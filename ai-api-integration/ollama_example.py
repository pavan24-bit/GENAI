"""
Ollama 
This program uses local AI models on your computer - no internet needed!
First, make sure you have Ollama installed and a model pulled:
Run this in terminal: ollama pull llama3.2
"""

import ollama

def query_ollama(prompt):
    """
    Send a prompt to local Ollama model and get response
    
    Args:
        prompt (str): Your question or instruction
        
    Returns:
        str: The AI's response or error message
    """
    try:
        # Use the chat interface
        response = ollama.chat(
            model='llama3.2',  # Make sure you've pulled this model first!
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ]
        )
        
        return response['message']['content']
        
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure Ollama is installed and running!\nRun: ollama pull llama3.2"

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("Ollama Local AI Program (No Internet Needed!)")
    print("=" * 50)
    print("\nNote: Make sure Ollama is running on your computer")
    print("If not running, open Terminal/CMD and type: ollama serve\n")
    
    user_prompt = input("Enter your question: ")
    
    if not user_prompt:
        print("Please enter something!")
    else:
        print("\n🤔 Thinking locally...")
        result = query_ollama(user_prompt)
        print("\n Response:")
        print("-" * 30)
        print(result)
        print("-" * 30)