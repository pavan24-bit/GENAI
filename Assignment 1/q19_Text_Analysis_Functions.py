#Q19 Text Analyzer 

print("=" * 40)
print("TEXT ANALYZER")
print("=" * 40)

text = input("Enter some text: ")

print("\nWhat do you want to know?")
print("1. Word count")
print("2. Vowel count")
print("3. Consonant count")
print("4. Reverse text")
print("5. Check palindrome")

choice = input("Enter choice (1-5): ")

if choice == "1":
    # Count words
    words = text.split()
    print(f"\nWord count: {len(words)}")

elif choice == "2":
    # Count vowels
    count = 0
    vowels = "aeiouAEIOU"
    for letter in text:
        if letter in vowels:
            count = count + 1
    print(f"\nVowel count: {count}")

elif choice == "3":
    # Count consonants
    count = 0
    vowels = "aeiouAEIOU"
    for letter in text:
        if letter.isalpha() and letter not in vowels:
            count = count + 1
    print(f"\nConsonant count: {count}")

elif choice == "4":
    # Reverse text
    print(f"\nReversed: {text[::-1]}")

elif choice == "5":
    # Check palindrome
    clean = text.replace(" ", "").lower()
    if clean == clean[::-1]:
        print("\n Yes, it's a palindrome!")
    else:
        print("\n No, it's not a palindrome")

else:
    print("Invalid choice!")

print("\nThanks for using Text Analyzer!")