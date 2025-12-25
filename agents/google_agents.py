import logging
import os
from dotenv import load_dotenv

from google.adk.runners import InMemoryRunner
from google.adk.agents.run_config import RunConfig
from google.genai import types
from google.genai.types import Content, Part

from agents.tools import fetch_genai_news, send_email
from google.adk.agents.llm_agent import LlmAgent

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class NewsAgent:
    """Google Multi-Agent for AI News Automation"""
    
    def __init__(self):
        """Initialize the Google agent with tools."""
        # Verify API key
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            logger.error("❌ ERROR: GOOGLE_API_KEY not found in .env file!")
            raise ValueError("GOOGLE_API_KEY not configured")
        else:
            logger.info(f"✅ API Key loaded: {api_key[:10]}...")
        
        # Initialize the agent with tools
        self.agent = LlmAgent(
            model='gemini-2.0-flash-exp',
            name='news_automation_agent',
            tools=[fetch_genai_news, send_email],
        )
        
        self.runner = None
        self.session = None
        
    async def run(self):
        """Execute the news automation workflow using Google agent."""
        try:
            logger.info("✅ Google agent initialized successfully")
            
            # Create a Runner
            self.runner = InMemoryRunner(
                app_name="AI_News_Automation",
                agent=self.agent,
            )
            
            # Create a Session
            self.session = await self.runner.session_service.create_session(
                app_name="AI_News_Automation",
                user_id="news_automation_user",
            )
            
            logger.info(f"✅ Session created: {self.session.id}")
            
            # Set response modality
            run_config = RunConfig(
                response_modalities=["TEXT"],
                session_resumption=types.SessionResumptionConfig()
            )
            
            # Create the prompt as a Content object with proper role
            prompt_text = (
                "You are an AI News Automation Agent. Your task:\n"
                "1. First, call the fetch_genai_news tool to get the latest Generative AI news\n"
                "2. Analyze and create a concise summary of the key findings\n"
                "3. Then, call the send_email tool to send the summary to devarajsharmila36@gmail.com\n"
                "4. Confirm when complete.\n\n"
                "Please execute these steps now."
            )
            
            # Create Content object with role
            new_message = Content(
                role="user",
                parts=[Part(text=prompt_text)]
            )
            
            logger.info("🚀 Starting agent execution...")
            
            # Run the agent with Content object
            full_response = []
            for event in self.runner.run(
                user_id="news_automation_user",
                session_id=self.session.id,
                new_message=new_message,
                run_config=run_config,
            ):
                logger.info(f"📨 Agent event: {event}")
                
                # Extract text from the event
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            full_response.append(part.text)
                            logger.info(f"✅ Agent response: {part.text}")
            
            logger.info("✅ Agent execution completed")
            
            response_text = ''.join(full_response)
            logger.info(f"📧 Full agent response: {response_text}")
            
            return response_text
            
        except Exception as e:
            logger.error(f"❌ Error in agent execution: {str(e)}")
            raise
