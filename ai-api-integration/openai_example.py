"""
OpenAI API 
This program uses OpenAI's GPT models to answer your questions.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (.env file)
load_dotenv()

def query_openai(prompt):
    """
    Send a prompt to OpenAI and get the response
    Args:
        prompt (str): Your question or instruction    
    Returns:
        str: The AI's response or error message
    """
    try:
        # Get API key from environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OpenAI API key not found! Please set the OPENAI_API_KEY environment variable."
        
        # Initialize the client
        client = OpenAI(api_key=api_key)
        
        # Make the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error: {str(e)}"

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("OpenAI Chat Program")
    print("=" * 50)
    
    # Get user input
    user_prompt = input("\nEnter your question or prompt: ")
    
    if not user_prompt:
        print("Please enter something!")
    else:
        print("\n🤔 Thinking...")
        result = query_openai(user_prompt)
        print("\n Response:")
        print("-" * 30)
        print(result)
        print("-" * 30)