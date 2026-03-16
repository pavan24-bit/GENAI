"""
Cohere 
This program uses Cohere's models to answer your questions.
"""

import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def query_cohere(prompt):
    """
    Send a prompt to Cohere using Chat API and get response
    Args:
        prompt (str): Your question or instruction
    Returns:
        str: The AI's response or error message
    """
    try:
        # Get API key
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            return "Error: Cohere API key not found!"
        
        # Initialize Cohere client with V2 (important!)
        co = cohere.ClientV2(api_key)
        
        # Use chat method instead of generate 
        response = co.chat(
            model="command-a-03-2025",  
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract response (different format than generate)
        return response.message.content[0].text
        
    except Exception as e:
        return f"Error: {str(e)}"

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("Cohere AI Program (Updated Chat API)")
    print("=" * 50)
    
    user_prompt = input("\nWhat would you like to ask? ")
    
    if not user_prompt:
        print("Please enter something!")
    else:
        print("\n🤔 Thinking...")
        result = query_cohere(user_prompt)
        print("\n Response:")
        print("-" * 30)
        print(result)
        print("-" * 30)