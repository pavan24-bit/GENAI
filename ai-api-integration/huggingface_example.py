"""
Hugging Face 
This program uses Hugging Face's models to answer your questions.
"""

from transformers import pipeline

# load model
generator = pipeline("text-generation", model="gpt2")

print("=" * 40)
print("🤖 HUGGING FACE SIMPLE AI")
print("=" * 40)

question = input("Ask me anything: ")

print("\n🤔 Thinking...\n")

result = generator(question, max_length=50)

print(" Answer:")
print("-" * 30)
print(result[0]["generated_text"])
print("-" * 30)