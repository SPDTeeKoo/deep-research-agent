import os
import requests
from typing import Dict

from agents import Agent, function_tool  # Keep as-is

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body using Resend"""
    
    # Get API key securely
    RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
    
    # Define sender and recipient
    from_email = "onboarding@resend.dev"  # Replace with your verified sender
    to_email = "tikusoumyo@gmail.com"      # Replace with your recipient
    
    # Prepare request headers
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    # Prepare email payload
    payload = {
        "from": f"SPD <{from_email}>",
        "to": [to_email],
        "subject": subject,
        "html": html_body
    }

    # Make API call
    response = requests.post("https://api.resend.com/emails", json=payload, headers=headers)
    
    # Log and return result
    print("Email response", response.status_code)
    if response.status_code == 202:
        return {"status": "success"}
    else:
        return {
            "status": "failure",
            "code": response.status_code,
            "message": response.text
        }

# Agent configuration
INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)
