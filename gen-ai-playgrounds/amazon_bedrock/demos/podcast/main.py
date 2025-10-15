from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import boto3
import json
import io
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS Clients
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

polly_client = boto3.client(
    service_name='polly',
    region_name='us-east-1'
)

class PodcastRequest(BaseModel):
    topic: str

class ScriptLine(BaseModel):
    speaker: str
    text: str

@app.post("/generate-script")
async def generate_script(request: PodcastRequest):
    """Generate podcast script using Amazon Bedrock"""
    
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

    try:
        # Call Claude via Bedrock
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
        script_text = response_body['content'][0]['text']
        print(script_text)

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
            raise ValueError("Failed to parse script format")

        return {"script": script}

    except Exception as e:
        print(f"Error details: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@app.post("/synthesize-speech")
async def synthesize_speech(line: ScriptLine):
    """Convert text to speech using Amazon Polly"""
    
    # Use Generative AI voices for more natural sound
    # Alex uses Matthew (Generative)
    # Sam uses Ruth (Generative)
    voice_id = 'Matthew' if line.speaker == 'ALEX' else 'Ruth'
    
    try:
        response = polly_client.synthesize_speech(
            Text=line.text,
            OutputFormat='mp3',
            VoiceId=voice_id,
            Engine='generative'  # Use generative engine instead of neural
        )

        # Stream the audio
        audio_stream = response['AudioStream'].read()
        
        return StreamingResponse(
            io.BytesIO(audio_stream),
            media_type="audio/mpeg"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "AI Podcast Generator API - Use /docs for documentation"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)