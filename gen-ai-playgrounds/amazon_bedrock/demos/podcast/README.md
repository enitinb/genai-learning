# 🎙️ AI Podcast Generator - Using Amazon Bedrock and polly

Generate natural, conversational podcasts on any topic using AI. Enter a topic and get a fully-voiced podcast with two hosts having a real conversation.

## ✨ Features

- 🤖 AI-generated scripts with natural dialogue (Claude Sonnet 4)
- 🎵 Realistic AI voices (Amazon Polly Generative)
- ⚡ Instant playback while generating
- 🎭 Natural timing with reactions and pauses
- 📝 Complete structure: intro, discussion, outro

## 🏗️ Architecture Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERACTION                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND (HTML/CSS/JS)                        │
│  • Enter Topic                                                   │
│  • Display Script                                                │
│  • Audio Queue & Player                                          │
│  • Smart Timing (200ms-600ms pauses)                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
        ┌──────────────────┐  ┌──────────────────┐
        │ POST             │  │ POST             │
        │ /generate-script │  │ /synthesize-     │
        │                  │  │ speech           │
        └──────────────────┘  └──────────────────┘
                    │                   │
                    ▼                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                             │
│  • Parse requests                                                │
│  • Call AWS APIs                                                 │
│  • Return JSON/Audio                                             │
└─────────────────────────────────────────────────────────────────┘
                    │                   │
                    ▼                   ▼
        ┌──────────────────┐  ┌──────────────────┐
        │ Amazon Bedrock   │  │ Amazon Polly     │
        │ Claude 4 Sonnet  │  │ Generative Voice │
        │                  │  │                  │
        │ Returns:         │  │ Returns:         │
        │ Script Array     │  │ MP3 Audio        │
        └──────────────────┘  └──────────────────┘
```

## 🤖 What the AI Does

**Bedrock (Claude Sonnet 4)** creates the script:
- Two hosts: Alex (enthusiastic) & Sam (knowledgeable)
- Natural reactions: "Wow!", "Right?", "Exactly!"
- Proper structure: welcome intro → discussion → thank you outro
- 15-20 exchanges with varied lengths

**Polly (Generative)** creates the voices:
- Alex → Matthew (male, conversational)
- Sam → Ruth (female, conversational)
- Ultra-realistic, human-like speech

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install fastapi uvicorn boto3 pydantic
```

### 2. Configure AWS

```bash
aws configure
# Enter: Access Key, Secret Key, Region (us-east-1 recommended)
```

### 3. Enable AWS Services

- **Bedrock:** AWS Console → Bedrock → Model access → Enable "Claude Sonnet 4"
- **Polly:** Ensure generative voices available in your region

### 4. Run

```bash
# Start backend
python main.py

# Open frontend
# Open podcast_frontend.html in browser
```

## 🎮 Usage

1. Enter a topic (e.g., "Space Exploration")
2. Click "Generate Podcast" → Wait for script
3. Click "Play Podcast" → Enjoy!

## 📁 Files

```
├── main.py        # FastAPI backend (2 endpoints)
├── podcast_frontend.html     # Frontend UI
└── README.md      # This file
```

## 🔧 Quick Customization

**Change Voices** (`main.py`):
```python
voice_id = 'Matthew' if line.speaker == 'ALEX' else 'Ruth'
# Options: Matthew, Ruth, Stephen, Gregory
```

**Adjust Timing** (`podcast_frontend.html`):
```javascript
pauseDuration = 200;  // Reactions: "Yeah!", "Wow!"
pauseDuration = 400;  // Questions
pauseDuration = 500;  // Default
pauseDuration = 600;  // Long statements
```

## 💡 Tech Stack

- **Backend:** FastAPI + Python
- **Frontend:** HTML/CSS/JavaScript
- **AI:** Amazon Bedrock (Claude 4) + Amazon Polly (Generative)