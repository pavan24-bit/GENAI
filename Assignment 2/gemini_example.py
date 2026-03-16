"""
Google Gemini 
This program uses Google's Gemini models to answer your questions.
"""

import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def query_gemini(prompt):
    """
    Send a prompt to Google Gemini and get response using new SDK
    Args:
        prompt (str): Your question or instruction
    Returns:
        str: The AI's response or error message
    """
    try:
        # Get API key
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Error: Google API key not found!"
        
        # Initialize the new client 
        client = genai.Client(api_key=api_key)
        
        # Use current model for content generation
        response = client.models.generate_content(
            model="gemini-2.5-flash",  
            contents=prompt
        )
        
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("Google Gemini AI Program (Updated SDK)")
    print("=" * 50)
    
    user_prompt = input("\nAsk Gemini anything: ")
    
    if not user_prompt:
        print("Please enter something!")
    else:
        print("\n🤔 Thinking...")
        result = query_gemini(user_prompt)
        print("\n Response:")
        print("-" * 30)
        print(result)
        print("-" * 30)