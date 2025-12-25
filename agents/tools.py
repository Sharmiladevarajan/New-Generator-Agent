import aiohttp
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")

async def fetch_genai_news():
    API_KEY = os.getenv("NEWSDATA_API_KEY")
    URL = "https://newsdata.io/api/1/news"

    params = {
        "apikey": API_KEY,
        "q": (
            '"Generative AI" OR "GenAI" OR "Google AI" OR '
            '"Gemini AI" OR "Vertex AI" OR "LLM" OR '
            '"agentic AI" OR "multimodal AI"'
        ),
        "language": "en",
        "category": "technology",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(URL, params=params, timeout=30) as resp:
            resp.raise_for_status()
            print("Fetched Generative AI news successfully.",resp.status)
            return await resp.json()
        
