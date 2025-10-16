from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import boto3
import json
import io
import re
import logging
import traceback
import asyncio
from typing import List, Optional, Literal, Callable, Any
from datetime import datetime, timedelta
from fastapi import Request
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(title="AI Podcast Generator API", version="1.0.0")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.now()
    
    # Log request
    logger.info(f"Request: {request.method} {request.url.path} from {request.client.host}")
    
    try:
        response = await call_next(request)
        
        # Log response
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"Response: {response.status_code} in {duration:.3f}s")
        
        return response
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        logger.error(f"Request failed: {request.method} {request.url.path} in {duration:.3f}s - {str(e)}")
        raise

# Global exception handlers
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Handle HTTP exceptions with enhanced logging and response format"""
    
    # Log the exception
    logger.warning(f"HTTP Exception: {exc.status_code} - {exc.detail} for {request.url.path}")
    
    # Return structured error response
    if isinstance(exc.detail, dict):
        # Already structured error
        return await http_exception_handler(request, exc)
    else:
        # Convert to structured error
        structured_error = create_error_response(
            "HTTP_ERROR",
            str(exc.detail),
            "Please check your request and try again"
        )
        exc.detail = structured_error
        return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle request validation errors with detailed feedback"""
    
    error_details = []
    for error in exc.errors():
        field = " -> ".join(str(loc) for loc in error["loc"])
        message = error["msg"]
        error_details.append(f"{field}: {message}")
    
    error_message = "Request validation failed: " + "; ".join(error_details)
    logger.warning(f"Validation error for {request.url.path}: {error_message}")
    
    structured_error = create_error_response(
        "VALIDATION_ERROR",
        error_message,
        "Please check your request format and required fields"
    )
    
    return HTTPException(status_code=422, detail=structured_error)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions with logging and safe error responses"""
    
    # Log the full exception with traceback
    logger.error(f"Unhandled exception for {request.url.path}: {str(exc)}", exc_info=True)
    
    # Don't expose internal details in production
    structured_error = create_error_response(
        "INTERNAL_SERVER_ERROR",
        "An unexpected error occurred while processing your request",
        "Please try again later or contact support if the problem persists"
    )
    
    return HTTPException(status_code=500, detail=structured_error)

# AWS Clients
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

polly_client = boto3.client(
    service_name='polly',
    region_name='us-east-1'
)

# Enhanced data models for multi-input support
class PodcastRequest(BaseModel):
    input_type: Literal['topic', 'file', 'text'] = 'topic'
    topic: Optional[str] = None
    content: Optional[str] = None
    
    def validate_input(self):
        """Validate that the appropriate field is provided for the input type"""
        if self.input_type == 'topic' and not self.topic:
            raise ValueError("Topic is required when input_type is 'topic'")
        elif self.input_type in ['file', 'text'] and not self.content:
            raise ValueError(f"Content is required when input_type is '{self.input_type}'")

class FileUploadResponse(BaseModel):
    filename: str
    content: str
    word_count: int
    file_type: str
    success: bool
    message: str

class ProcessedContent(BaseModel):
    original_word_count: int
    processed_content: str
    final_word_count: int
    was_summarized: bool

class ContentSummaryResponse(BaseModel):
    original_content: str
    summarized_content: str
    original_word_count: int
    final_word_count: int

class ScriptLine(BaseModel):
    speaker: str
    text: str

class ErrorResponse(BaseModel):
    error: str
    detail: str
    timestamp: str
    suggestion: Optional[str] = None

class ProcessingStatus(BaseModel):
    step: str
    status: str
    message: str
    progress: Optional[int] = None



# Enhanced error handling utilities
def create_error_response(error_type: str, detail: str, suggestion: str = None) -> dict:
    """Create standardized error response"""
    return {
        "error": error_type,
        "detail": detail,
        "timestamp": datetime.now().isoformat(),
        "suggestion": suggestion
    }

def log_error(operation: str, error: Exception, context: dict = None):
    """Log errors with context information"""
    error_info = {
        "operation": operation,
        "error_type": type(error).__name__,
        "error_message": str(error),
        "timestamp": datetime.now().isoformat()
    }
    if context:
        error_info.update(context)
    
    logger.error(f"Error in {operation}: {error_info}")
    return error_info

# Retry and circuit breaker utilities
class CircuitBreaker:
    """Simple circuit breaker implementation for external service calls"""
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def can_execute(self) -> bool:
        """Check if the circuit breaker allows execution"""
        if self.state == "CLOSED":
            return True
        elif self.state == "OPEN":
            if self.last_failure_time and \
               datetime.now() - self.last_failure_time > timedelta(seconds=self.recovery_timeout):
                self.state = "HALF_OPEN"
                return True
            return False
        else:  # HALF_OPEN
            return True
    
    def record_success(self):
        """Record a successful operation"""
        self.failure_count = 0
        self.state = "CLOSED"
    
    def record_failure(self):
        """Record a failed operation"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"

# Circuit breakers for external services
bedrock_circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=30)
polly_circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=30)

async def retry_with_backoff(
    func: Callable,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 10.0,
    backoff_factor: float = 2.0,
    circuit_breaker: CircuitBreaker = None
) -> Any:
    """Retry function with exponential backoff and optional circuit breaker"""
    
    if circuit_breaker and not circuit_breaker.can_execute():
        raise Exception("Circuit breaker is OPEN - service temporarily unavailable")
    
    last_exception = None
    
    for attempt in range(max_retries + 1):
        try:
            result = await func() if asyncio.iscoroutinefunction(func) else func()
            
            if circuit_breaker:
                circuit_breaker.record_success()
            
            return result
            
        except Exception as e:
            last_exception = e
            
            if circuit_breaker:
                circuit_breaker.record_failure()
            
            if attempt == max_retries:
                break
            
            # Calculate delay with exponential backoff
            delay = min(base_delay * (backoff_factor ** attempt), max_delay)
            logger.warning(f"Attempt {attempt + 1} failed, retrying in {delay:.2f}s: {str(e)}")
            await asyncio.sleep(delay)
    
    raise last_exception

# Content processing utilities
def count_words(text: str) -> int:
    """Count words in text, handling various whitespace and punctuation"""
    if not text:
        return 0
    # Remove extra whitespace and split on whitespace
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)

def validate_content_length(text: str, min_words: int = 50, max_words: int = 10000) -> tuple[bool, str]:
    """Validate content length and return validation result with message"""
    if not text or not text.strip():
        return False, "Content cannot be empty"
    
    word_count = count_words(text)
    
    if word_count < min_words:
        return False, f"Content too short. Minimum {min_words} words required, got {word_count} words."
    
    if word_count > max_words:
        return False, f"Content too long. Maximum {max_words} words allowed, got {word_count} words."
    
    return True, f"Content length valid: {word_count} words"

def clean_content(text: str) -> str:
    """Clean and preprocess content for better processing"""
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove excessive newlines but preserve paragraph breaks
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text

def needs_summarization(text: str, word_limit: int = 2000) -> bool:
    """Check if content needs summarization based on word count"""
    return count_words(text) > word_limit

async def summarize_content(content: str, target_words: int = 1800) -> str:
    """Summarize content using Claude with retry logic and circuit breaker"""
    
    original_word_count = count_words(content)
    
    prompt = f"""Please summarize the following content to approximately {target_words} words while preserving all key information, main points, and important details. The summary should be comprehensive enough to create an engaging podcast discussion.

ORIGINAL CONTENT ({original_word_count} words):
{content}

REQUIREMENTS:
- Target length: approximately {target_words} words
- Preserve all key concepts and main points
- Maintain the logical flow and structure
- Keep important examples and details that would make for good podcast discussion
- Write in clear, conversational language suitable for podcast hosts to discuss

SUMMARY:"""

    async def call_bedrock():
        """Make the actual Bedrock API call"""
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 3000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3
        })

        response = bedrock_runtime.invoke_model(
            modelId='us.anthropic.claude-sonnet-4-20250514-v1:0',
            body=body
        )

        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text'].strip()

    try:
        # Use retry logic with circuit breaker
        summarized_content = await retry_with_backoff(
            call_bedrock,
            max_retries=2,
            base_delay=1.0,
            circuit_breaker=bedrock_circuit_breaker
        )
        
        # Verify the summary is actually shorter
        summary_word_count = count_words(summarized_content)
        if summary_word_count >= original_word_count:
            # If summary isn't shorter, try a more aggressive approach
            return await summarize_content_aggressive(content, target_words)
        
        return summarized_content

    except Exception as e:
        logger.error(f"Summarization failed after retries: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error summarizing content: {str(e)}"
        )

async def summarize_content_aggressive(content: str, target_words: int = 1500) -> str:
    """More aggressive summarization as fallback with retry logic"""
    
    prompt = f"""Create a concise summary of the following content in exactly {target_words} words or fewer. Focus only on the most essential points:

{content}

Summary ({target_words} words max):"""

    async def call_bedrock_aggressive():
        """Make the aggressive summarization API call"""
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2
        })

        response = bedrock_runtime.invoke_model(
            modelId='us.anthropic.claude-sonnet-4-20250514-v1:0',
            body=body
        )

        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text'].strip()

    try:
        return await retry_with_backoff(
            call_bedrock_aggressive,
            max_retries=2,
            base_delay=1.0,
            circuit_breaker=bedrock_circuit_breaker
        )

    except Exception as e:
        logger.error(f"Aggressive summarization failed after retries: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error in aggressive summarization: {str(e)}"
        )

def validate_file_type(filename: str) -> bool:
    """Validate if file type is supported"""
    supported_extensions = ['.txt', '.md', '.pdf', '.docx']
    return any(filename.lower().endswith(ext) for ext in supported_extensions)

def extract_text_from_file(file_content: bytes, filename: str) -> str:
    """Extract text from uploaded file based on file type"""
    try:
        if filename.lower().endswith(('.txt', '.md')):
            # Handle text and markdown files
            return file_content.decode('utf-8')
        elif filename.lower().endswith('.pdf'):
            # Handle PDF files
            return extract_text_from_pdf(file_content)
        elif filename.lower().endswith('.docx'):
            # Handle DOCX files
            return extract_text_from_docx(file_content)
        else:
            raise ValueError(f"Unsupported file type: {filename}")
    except UnicodeDecodeError:
        raise ValueError("File encoding not supported. Please use UTF-8 encoded files.")

def extract_text_from_pdf(file_content: bytes) -> str:
    """Extract text from PDF file"""
    try:
        import PyPDF2
        pdf_file = io.BytesIO(file_content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        if not text.strip():
            raise ValueError("PDF file contains no extractable text")
        
        return text.strip()
    except ImportError:
        raise ValueError("PDF processing not available. Please install PyPDF2: pip install PyPDF2")
    except Exception as e:
        raise ValueError(f"Error reading PDF file: {str(e)}")

def extract_text_from_docx(file_content: bytes) -> str:
    """Extract text from DOCX file"""
    try:
        import docx
        docx_file = io.BytesIO(file_content)
        doc = docx.Document(docx_file)
        
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        if not text.strip():
            raise ValueError("DOCX file contains no readable text")
        
        return text.strip()
    except ImportError:
        raise ValueError("DOCX processing not available. Please install python-docx: pip install python-docx")
    except Exception as e:
        raise ValueError(f"Error reading DOCX file: {str(e)}")

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    """Upload and process a file for podcast generation with enhanced error handling"""
    
    operation_context = {
        "filename": file.filename,
        "content_type": file.content_type,
        "operation": "file_upload"
    }
    
    logger.info(f"Starting file upload: {file.filename}")
    
    try:
        # Validate file type
        if not validate_file_type(file.filename):
            error_detail = f"Unsupported file format: {file.filename}. Supported formats: .txt, .md, .pdf, .docx"
            logger.warning(error_detail)
            raise HTTPException(
                status_code=400, 
                detail=create_error_response(
                    "UNSUPPORTED_FILE_FORMAT",
                    error_detail,
                    "Please convert your file to one of the supported formats: TXT, MD, PDF, or DOCX"
                )
            )
        
        # Check file size (10MB limit)
        max_size = 10 * 1024 * 1024  # 10MB
        file_content = await file.read()
        file_size_mb = len(file_content) / 1024 / 1024
        
        operation_context["file_size_mb"] = round(file_size_mb, 2)
        
        if len(file_content) > max_size:
            error_detail = f"File too large: {file_size_mb:.2f}MB. Maximum size is 10MB."
            logger.warning(error_detail)
            raise HTTPException(
                status_code=413,
                detail=create_error_response(
                    "FILE_TOO_LARGE",
                    error_detail,
                    "Please reduce your file size or split the content into smaller files"
                )
            )
        
        if len(file_content) == 0:
            error_detail = "Empty file uploaded. Please upload a file with content."
            logger.warning(error_detail)
            raise HTTPException(
                status_code=400,
                detail=create_error_response(
                    "EMPTY_FILE",
                    error_detail,
                    "Ensure your file contains text content before uploading"
                )
            )
        
        logger.info(f"File validation passed: {file.filename} ({file_size_mb:.2f}MB)")
        
        # Extract text content
        text_content = extract_text_from_file(file_content, file.filename)
        
        if not text_content.strip():
            error_detail = "File contains no readable text content."
            logger.warning(f"No text extracted from {file.filename}")
            raise HTTPException(
                status_code=400,
                detail=create_error_response(
                    "NO_TEXT_CONTENT",
                    error_detail,
                    "Ensure your file contains readable text. For PDFs, make sure the text is not in image format."
                )
            )
        
        # Count words and validate content
        word_count = count_words(text_content)
        operation_context["word_count"] = word_count
        
        if word_count < 50:
            error_detail = f"Content too short: {word_count} words. Minimum 50 words required."
            logger.warning(error_detail)
            raise HTTPException(
                status_code=400,
                detail=create_error_response(
                    "CONTENT_TOO_SHORT",
                    error_detail,
                    "Please provide more content or combine with additional material"
                )
            )
        
        # Determine file type
        file_extension = file.filename.lower().split('.')[-1] if '.' in file.filename else 'unknown'
        
        logger.info(f"File processed successfully: {file.filename} - {word_count} words")
        
        return FileUploadResponse(
            filename=file.filename,
            content=text_content,
            word_count=word_count,
            file_type=file_extension,
            success=True,
            message=f"File uploaded successfully. Contains {word_count} words."
        )
        
    except HTTPException:
        raise
    except ValueError as e:
        log_error("file_upload", e, operation_context)
        raise HTTPException(
            status_code=422, 
            detail=create_error_response(
                "FILE_PROCESSING_ERROR",
                str(e),
                "Check that your file is not corrupted and contains valid text content"
            )
        )
    except Exception as e:
        log_error("file_upload", e, operation_context)
        raise HTTPException(
            status_code=500, 
            detail=create_error_response(
                "INTERNAL_SERVER_ERROR",
                f"Unexpected error processing file: {str(e)}",
                "Please try again or contact support if the problem persists"
            )
        )

@app.post("/process-content")
async def process_content_endpoint(request: dict):
    """Process content for podcast generation with enhanced error handling and status updates"""
    
    content = request.get('content', '')
    input_type = request.get('input_type', 'text')
    
    operation_context = {
        "input_type": input_type,
        "content_length": len(content),
        "operation": "content_processing"
    }
    
    logger.info(f"Starting content processing: {input_type} input, {len(content)} characters")
    
    if not content:
        error_detail = "Content is required for processing"
        logger.warning(error_detail)
        raise HTTPException(
            status_code=400, 
            detail=create_error_response(
                "MISSING_CONTENT",
                error_detail,
                "Please provide content to process"
            )
        )
    

    
    try:
        # Clean and validate content
        logger.info("Cleaning and validating content...")
        cleaned_content = clean_content(content)
        is_valid, validation_message = validate_content_length(cleaned_content)
        
        if not is_valid:
            logger.warning(f"Content validation failed: {validation_message}")
            raise HTTPException(
                status_code=400, 
                detail=create_error_response(
                    "CONTENT_VALIDATION_FAILED",
                    validation_message,
                    "Please adjust your content length to meet the requirements"
                )
            )
        
        original_word_count = count_words(cleaned_content)
        operation_context["original_word_count"] = original_word_count
        
        logger.info(f"Content validated: {original_word_count} words")
        
        # Check if summarization is needed
        if needs_summarization(cleaned_content):
            logger.info(f"Content requires summarization ({original_word_count} > 2000 words)")
            
            try:
                summarized_content = await summarize_content(cleaned_content)
                final_word_count = count_words(summarized_content)
                operation_context["final_word_count"] = final_word_count
                
                logger.info(f"Content summarized: {original_word_count} → {final_word_count} words")
                
                return ProcessedContent(
                    original_word_count=original_word_count,
                    processed_content=summarized_content,
                    final_word_count=final_word_count,
                    was_summarized=True
                )
            except Exception as e:
                log_error("content_summarization", e, operation_context)
                raise HTTPException(
                    status_code=500,
                    detail=create_error_response(
                        "SUMMARIZATION_FAILED",
                        f"Failed to summarize content: {str(e)}",
                        "Try reducing your content length manually or check your AWS Bedrock access"
                    )
                )
        else:
            logger.info(f"Content within limits, no summarization needed ({original_word_count} words)")
            return ProcessedContent(
                original_word_count=original_word_count,
                processed_content=cleaned_content,
                final_word_count=original_word_count,
                was_summarized=False
            )
            
    except HTTPException:
        raise
    except Exception as e:
        log_error("content_processing", e, operation_context)
        raise HTTPException(
            status_code=500,
            detail=create_error_response(
                "CONTENT_PROCESSING_ERROR",
                f"Unexpected error during content processing: {str(e)}",
                "Please try again or contact support if the problem persists"
            )
        )

@app.post("/summarize-content")
async def summarize_content_endpoint(request: dict):
    """Summarize content if it exceeds word limit"""
    
    content = request.get('content', '')
    if not content:
        raise HTTPException(status_code=400, detail="Content is required")
    
    original_word_count = count_words(content)
    
    if not needs_summarization(content):
        return ContentSummaryResponse(
            original_content=content,
            summarized_content=content,
            original_word_count=original_word_count,
            final_word_count=original_word_count
        )
    
    try:
        summarized = await summarize_content(content)
        final_word_count = count_words(summarized)
        
        return ContentSummaryResponse(
            original_content=content,
            summarized_content=summarized,
            original_word_count=original_word_count,
            final_word_count=final_word_count
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Summarization failed: {str(e)}"
        )

@app.post("/generate-script")
async def generate_script(request: PodcastRequest):
    """Generate podcast script using Amazon Bedrock"""
    
    # Validate input based on type
    try:
        request.validate_input()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Generate appropriate prompt based on input type
    if request.input_type == 'topic':
        prompt = f"""Generate a natural, engaging podcast conversation between two hosts about: {request.topic}

Make it conversational with:
- Host 1 (Alex - enthusiastic, curious voice)
- Host 2 (Sam - knowledgeable, thoughtful voice)

STRUCTURE:
1. START with a warm welcome and intro (both hosts greeting listeners and introducing the topic)
2. MIDDLE: Natural conversation about the topic
3. END with thanks to listeners and a sign-off (both hosts saying goodbye and thanking for listening)

IMPORTANT: Make it feel like a REAL conversation with:
- Natural reactions and interjections (like "Oh wow!", "Right?", "Exactly!", "Hmm", "Yeah")
- Back-channel responses where one person reacts while the other is speaking
- Occasional agreement sounds and acknowledgments
- Sometimes shorter, punchy responses mixed with longer explanations
- Natural flow with questions and answers

Format as:
ALEX: [their dialogue]
SAM: [short reaction like "Mm-hmm" or "Yeah"]
ALEX: [continues]
SAM: [their full response]
ALEX: [reaction] [question]
etc.

Include reactions like:
- "Oh!", "Wow!", "Really?", "Interesting!", "Right!", "Exactly!"
- "Mm-hmm", "Yeah", "Uh-huh", "I see"
- "That's wild!", "No way!", "For sure!"

EXAMPLE OPENING:
ALEX: Hey everyone! Welcome back to the podcast!
SAM: Great to have you here!
ALEX: Today we're talking about [topic]. Sam, I'm really excited about this one.
SAM: Me too! This is fascinating stuff.

EXAMPLE ENDING:
ALEX: Well, that's all the time we have for today.
SAM: Yeah, this was a great conversation!
ALEX: Thanks so much for listening, everyone!
SAM: Until next time, take care!
ALEX: See you soon!

Keep it to about 15-20 exchanges total with natural back-and-forth."""
    
    else:  # input_type is 'file' or 'text'
        # Check if content needs summarization
        content_to_use = request.content
        if needs_summarization(request.content):
            try:
                content_to_use = await summarize_content(request.content)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Content summarization failed: {str(e)}"
                )
        
        prompt = f"""Convert the following content into a natural, engaging podcast conversation between two hosts:

CONTENT TO DISCUSS:
{content_to_use}

Create a conversation with:
- Host 1 (Alex - enthusiastic, curious voice)
- Host 2 (Sam - knowledgeable, thoughtful voice)

STRUCTURE:
1. START with a warm welcome and brief intro to the topic
2. MIDDLE: Natural conversation covering the key points from the content
3. END with thanks to listeners and a sign-off

IMPORTANT: Make it feel like a REAL conversation with:
- Natural reactions and interjections (like "Oh wow!", "Right?", "Exactly!", "Hmm", "Yeah")
- Back-channel responses where one person reacts while the other is speaking
- Occasional agreement sounds and acknowledgments
- Sometimes shorter, punchy responses mixed with longer explanations
- Natural flow with questions and answers about the content

The hosts should discuss the main points from the provided content in a conversational way, asking each other questions and building on each other's points.

Format as:
ALEX: [their dialogue]
SAM: [short reaction like "Mm-hmm" or "Yeah"]
ALEX: [continues]
SAM: [their full response]
ALEX: [reaction] [question]
etc.

Include reactions like:
- "Oh!", "Wow!", "Really?", "Interesting!", "Right!", "Exactly!"
- "Mm-hmm", "Yeah", "Uh-huh", "I see"
- "That's wild!", "No way!", "For sure!"

Keep it to about 15-20 exchanges total with natural back-and-forth covering the key information."""

    async def generate_script_content():
        """Generate script content with Bedrock API call"""
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 3000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.9
        })

        response = bedrock_runtime.invoke_model(
            modelId='us.anthropic.claude-sonnet-4-20250514-v1:0',
            body=body
        )

        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text']

    try:
        # Use retry logic with circuit breaker for script generation
        script_text = await retry_with_backoff(
            generate_script_content,
            max_retries=2,
            base_delay=1.0,
            circuit_breaker=bedrock_circuit_breaker
        )

        # Parse the script
        lines = script_text.strip().split('\n')
        script = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('ALEX:'):
                script.append({
                    "speaker": "ALEX",
                    "text": line.replace('ALEX:', '').strip()
                })
            elif line.startswith('SAM:'):
                script.append({
                    "speaker": "SAM",
                    "text": line.replace('SAM:', '').strip()
                })

        if len(script) == 0:
            # Fallback if parsing fails
            raise ValueError("Failed to parse script format - no valid speaker lines found")

        logger.info(f"Script generated successfully: {len(script)} lines")
        return {"script": script}

    except Exception as e:
        operation_context = {
            "input_type": request.input_type,
            "topic": request.topic if request.input_type == 'topic' else None,
            "content_length": len(request.content) if request.content else 0,
            "operation": "script_generation"
        }
        
        log_error("script_generation", e, operation_context)
        
        # Provide specific error messages based on error type
        if "bedrock" in str(e).lower() or "anthropic" in str(e).lower():
            error_detail = "AI service unavailable. Please check your AWS Bedrock configuration."
            suggestion = "Ensure AWS credentials are configured and you have access to Claude models in Bedrock"
        elif "timeout" in str(e).lower():
            error_detail = "Request timed out. The AI service took too long to respond."
            suggestion = "Try again with shorter content or check your network connection"
        else:
            error_detail = f"Script generation failed: {str(e)}"
            suggestion = "Please try again or contact support if the problem persists"
        
        raise HTTPException(
            status_code=500, 
            detail=create_error_response(
                "SCRIPT_GENERATION_FAILED",
                error_detail,
                suggestion
            )
        )


@app.post("/synthesize-speech")
async def synthesize_speech(line: ScriptLine):
    """Convert text to speech using Amazon Polly with enhanced error handling"""
    
    operation_context = {
        "speaker": line.speaker,
        "text_length": len(line.text),
        "operation": "speech_synthesis"
    }
    
    logger.info(f"Synthesizing speech for {line.speaker}: {len(line.text)} characters")
    
    # Use Generative AI voices for more natural sound
    voice_id = 'Matthew' if line.speaker == 'ALEX' else 'Ruth'
    
    async def synthesize_speech_call():
        """Make the Polly API call for speech synthesis"""
        response = polly_client.synthesize_speech(
            Text=line.text,
            OutputFormat='mp3',
            VoiceId=voice_id,
            Engine='generative'
        )
        return response['AudioStream'].read()

    try:
        # Use retry logic with circuit breaker for speech synthesis
        audio_stream = await retry_with_backoff(
            synthesize_speech_call,
            max_retries=2,
            base_delay=0.5,
            circuit_breaker=polly_circuit_breaker
        )
        
        logger.info(f"Speech synthesis successful for {line.speaker}")
        
        return StreamingResponse(
            io.BytesIO(audio_stream),
            media_type="audio/mpeg"
        )

    except Exception as e:
        log_error("speech_synthesis", e, operation_context)
        
        if "polly" in str(e).lower() or "aws" in str(e).lower():
            error_detail = "Speech synthesis service unavailable. Please check your AWS Polly configuration."
            suggestion = "Ensure AWS credentials are configured and you have access to Polly service"
        else:
            error_detail = f"Speech synthesis failed: {str(e)}"
            suggestion = "Please try again or contact support if the problem persists"
        
        raise HTTPException(
            status_code=500, 
            detail=create_error_response(
                "SPEECH_SYNTHESIS_FAILED",
                error_detail,
                suggestion
            )
        )

@app.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }




@app.get("/")
async def root():
    return {"message": "AI Podcast Generator API - Use /docs for documentation"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
