"""
Groq API 
This program uses Groq's Llama models (super fast!) to answer your questions.
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def query_groq(prompt):
    """
    Send a prompt to Groq and get the response
    Args:
        prompt (str): Your question or instruction
    Returns:
        str: The AI's response or error message
    """
    try:
        # Get API key from environment variable
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "Error: Groq API key not found! Please set the GROQ_API_KEY environment variable."
        
        # Initialize the client
        client = Groq(api_key=api_key)
        
        # Make the API call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Fast and free model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error: {str(e)}"

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("Groq Chat Program (Super Fast!)")
    print("=" * 50)
    
    user_prompt = input("\nWhat would you like to ask? ")
    
    if not user_prompt:
        print("Please enter something!")
    else:
        print("\n⚡ Thinking (this will be fast!)...")
        result = query_groq(user_prompt)
        print("\n Response:")
        print("-" * 30)
        print(result)
        print("-" * 30)