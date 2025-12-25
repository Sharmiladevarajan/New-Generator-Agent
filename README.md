# AI News Automation System

An intelligent Python application that automatically fetches the latest Generative AI news, generates AI-powered summaries using Google Gemini, and delivers them via email every 5 hours.

## 🌟 Features

- 🤖 **Google AI Agent**: Powered by Gemini 1.5 Flash for intelligent news summarization
- 📰 **News Fetching**: Retrieves latest Generative AI news from NewsData.io API
- 📝 **AI Summarization**: Creates concise, professional summaries using Google Gemini
- 📧 **Email Delivery**: Sends formatted news summaries to devarajsharmila36@gmail.com
- ⏰ **Automatic Scheduling**: Runs every 5 hours continuously
- 🔄 **Async Architecture**: Efficient asynchronous execution with proper error handling

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
# Google Gemini API Key (Get from https://aistudio.google.com/app/apikey)
GOOGLE_API_KEY=your_gemini_api_key_here

# SMTP Email Settings
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# News API Settings (Get from https://newsdata.io)
NEWS_API_KEY=your_newsdata_api_key_here
```

### 3. Run the Application

```bash
python main.py
```

The system will:
- ✅ Execute immediately on startup
- ✅ Fetch latest Generative AI news
- ✅ Generate AI-powered summary with Gemini
- ✅ Send email to devarajsharmila36@gmail.com
- ✅ Schedule itself to run every 5 hours automatically

## 📁 Project Structure

```
AI News Automation/
├── main.py                      # Main entry point with 5-hour scheduling
├── agents/
│   ├── google_agents.py         # NewsAgent - main orchestrator with Gemini AI
│   └── tools.py                 # fetch_genai_news & send_email tools
├── .env                         # Environment variables (create this)
├── .env.example                 # Example environment file
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🔧 How It Works

### Workflow Architecture

```
main.py
   ↓
NewsAgent (Google Gemini AI)
   ↓
1. fetch_genai_news() → Fetches latest news from NewsData.io
   ↓
2. Gemini AI → Generates professional summary
   ↓
3. send_email() → Sends to devarajsharmila36@gmail.com
   ↓
Schedule next run in 5 hours
```

### Components

#### 1. **NewsAgent** (`agents/google_agents.py`)
- Main orchestrator powered by Google Gemini 1.5 Flash
- Manages the complete workflow
- Uses AI to generate intelligent summaries
- Handles errors and logging

#### 2. **Tools** (`agents/tools.py`)
- **fetch_genai_news()**: Fetches Generative AI news from NewsData.io API
- **send_email()**: Sends formatted emails via SMTP to devarajsharmila36@gmail.com

#### 3. **Main Scheduler** (`main.py`)
- Executes agent immediately on startup
- Schedules recurring execution every 5 hours
- Keeps the system running continuously

## 🔑 API Keys Setup

### Google Gemini API (FREE)
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key (starts with `AIzaSy...`)
5. Add to `.env` file

**Free Tier Limits:**
- 15 requests per minute
- 1M tokens per minute
- 1,500 requests per day

### NewsData.io API (FREE)
1. Visit [NewsData.io](https://newsdata.io/register)
2. Sign up for a free account
3. Get your API key from dashboard
4. Add to `.env` file

**Free Tier Limits:**
- 200 requests per day
- Perfect for 5-hour scheduling (max 5 calls/day)

### Gmail App Password (for SMTP)
1. Enable 2-Factor Authentication on Gmail
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate new app password
4. Use this password in `.env` (not your regular password)

## 📦 Dependencies

```
aiohttp==3.9.1              # Async HTTP client for news fetching
python-dotenv==1.0.0        # Environment variable management
schedule==1.2.0             # Job scheduling every 5 hours
google-generativeai==0.8.3  # Google Gemini AI integration
requests==2.31.0            # HTTP requests
```

## 🎯 Configuration

### Target Email
Currently configured to send to: **devarajsharmila36@gmail.com**

To change the recipient, update in `agents/google_agents.py`:
```python
await send_email(
    to_email="new_email@example.com",  # Change here
    subject="Latest Generative AI News Summary",
    body=summary
)
```

### Scheduling Interval
Default: **5 hours**

To change, update in `main.py`:
```python
schedule.every(5).hours.do(schedule_job)  # Change the number
```

## 📊 Example Output

### Console Output
```
2025-12-25 20:00:00 - __main__ - INFO - Starting AI News Automation System
2025-12-25 20:00:00 - agents.google_agents - INFO - ✅ API Key loaded: AIzaSyBMxg...
2025-12-25 20:00:00 - agents.google_agents - INFO - ✅ NewsAgent initialized successfully
2025-12-25 20:00:01 - agents.google_agents - INFO - 🔍 Step 1: Fetching Generative AI news...
2025-12-25 20:00:02 - agents.google_agents - INFO - ✅ Fetched 10 articles
2025-12-25 20:00:02 - agents.google_agents - INFO - 🤖 Generating summary with Gemini AI...
2025-12-25 20:00:04 - agents.google_agents - INFO - ✅ Summary generated successfully
2025-12-25 20:00:04 - agents.google_agents - INFO - 📧 Step 3: Sending email to devarajsharmila36@gmail.com...
2025-12-25 20:00:05 - agents.google_agents - INFO - ✅ Email sent successfully
2025-12-25 20:00:05 - __main__ - INFO - Agent scheduled to run every 5 hours
```

### Email Example
**Subject:** Latest Generative AI News Summary

**Body:**
```
The latest developments in Generative AI showcase significant breakthroughs across 
multiple fronts. OpenAI's recent GPT-4 Turbo update brings enhanced reasoning 
capabilities and reduced costs, while Google's Gemini Pro continues to demonstrate 
impressive multimodal understanding...

Key trends include increased focus on AI safety, democratization of AI tools for 
developers, and growing enterprise adoption. Notable announcements feature new 
partnerships between major tech companies and startups pushing the boundaries of 
what's possible with generative models.
```

## 🛠️ Development

### Testing Individual Components

Test news fetching:
```python
import asyncio
from agents.tools import fetch_genai_news

async def test():
    news = await fetch_genai_news()
    print(f"Fetched {len(news['articles'])} articles")

asyncio.run(test())
```

Test email sending:
```python
import asyncio
from agents.tools import send_email

async def test():
    result = await send_email(
        to_email="test@example.com",
        subject="Test",
        body="This is a test"
    )
    print(result)

asyncio.run(test())
```

## 🐛 Troubleshooting

### Common Issues

**1. API Key Invalid**
- Ensure no quotes around the key in `.env`
- Verify key starts with `AIzaSy`
- Check if key is enabled in Google AI Studio

**2. No Emails Received**
- Check spam folder
- Verify SMTP credentials
- Ensure Gmail App Password is used (not regular password)
- Check if 2FA is enabled on Gmail

**3. News Not Fetching**
- Verify NewsData.io API key
- Check if daily limit (200 requests) is reached
- Ensure internet connection is stable

**4. Module Import Errors**
```bash
pip install --upgrade -r requirements.txt
```

## 📝 Logs

Logs are displayed in console with detailed information:
- ✅ Success messages (green indicators)
- 🔍 Processing steps
- ❌ Error messages with full traceback
- 📊 Statistics (articles fetched, email sent, etc.)

## 🔒 Security Notes

- ⚠️ Never commit `.env` file to version control
- ✅ Use environment variables for all sensitive data
- ✅ Use Gmail App Passwords, not regular passwords
- ✅ Keep API keys secret and rotate them regularly

## 🚀 Production Deployment

For production use:
1. Use a process manager like `systemd` or `supervisor`
2. Set up proper logging to files
3. Add monitoring and alerting
4. Use a proper SMTP service (SendGrid, AWS SES)
5. Implement retry logic for failed requests
6. Add database for tracking sent emails

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

This is a personal automation project, but suggestions are welcome!

## 📧 Contact

Email recipient: devarajsharmila36@gmail.com

---

**Status:** ✅ Production Ready | **Version:** 1.0.0 | **Last Updated:** December 25, 2025