#!/usr/bin/env python3
"""
AI News Automation System
Main entry point that triggers the Google agent to fetch, summarize and email news.
"""

import asyncio
import logging
import schedule
import time
from agents.google_agents import NewsAgent
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def run_agent():
    """Execute the Google agent workflow."""
    try:
        logger.info("Starting AI News Automation System")
        
        # Initialize the Google agent
        agent = NewsAgent()
        
        # Execute the complete news automation flow
        await agent.run()
        
        logger.info("News automation completed successfully")
        
    except Exception as e:
        logger.error(f"Error in news automation: {str(e)}")

def schedule_job():
    """Wrapper to run async agent in sync context."""
    asyncio.run(run_agent())

async def main():
    """Main execution with 5-hour scheduling."""
    # Run immediately on start
    await run_agent()
    
    # Schedule to run every 5 hours
    schedule.every(5).hours.do(schedule_job)
    
    logger.info("Agent scheduled to run every 5 hours")
    
    # Keep the script running to execute scheduled tasks
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)  # Check every minute

if __name__ == "__main__":
    asyncio.run(main())