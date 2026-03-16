# Q17 Palindrome Checker 

print("PALINDROME CHECKER")
print("==================")

word = input("Enter a word or number: ")

# Convert to lowercase
lower_word = word.lower()

# Reverse
reversed_word = lower_word[::-1]

# Check
if lower_word == reversed_word:
    print(f"\n {word} is a PALINDROME!")
    print(f"Forward: {word}")
    print(f"Backward: {word[::-1]}")
else:
    print(f"\n {word} is NOT a palindrome!")
    print(f"Forward: {word}")
    print(f"Backward: {word[::-1]}")