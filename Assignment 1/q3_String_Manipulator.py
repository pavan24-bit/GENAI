# Question 3: String Manipulator
print("=" * 50)
print("        STRING MANIPULATOR PROGRAM")
print("=" * 50)
print()

# Taking sentence
sentence = input("Enter a sentence: ")

print("\n" + "-" * 50)
print("           RESULTS")
print("-" * 50)

# 1. Original sentence
print("1. Original:", sentence)

# 2. Characters with spaces
char_with_spaces = len(sentence)
print("2. Characters (with spaces):", char_with_spaces)

# 3. Characters without spaces
sentence_no_spaces = sentence.replace(" ", "")
char_without_spaces = len(sentence_no_spaces)
print("3. Characters (without spaces):", char_without_spaces)

# 4. Total words
words_list = sentence.split()
word_count = len(words_list)
print("4. Total words:", word_count)

# 5. UPPERCASE
uppercase_sentence = sentence.upper()
print("5. UPPERCASE:", uppercase_sentence)

# 6. lowercase
lowercase_sentence = sentence.lower()
print("6. lowercase:", lowercase_sentence)

# 7. Title Case
title_case_sentence = sentence.title()
print("7. Title Case:", title_case_sentence)

# 8. First word
if len(words_list) > 0:  
    first_word = words_list[0]
    print("8. First word:", first_word)
else:
    print("8. First word: (no words)")

# 9. Last word
if len(words_list) > 0:
    last_word = words_list[-1]
    print("9. Last word:", last_word)
else:
    print("9. Last word: (no words)")

# 10. Reversed sentence
reversed_sentence = sentence[::-1]
print("10. Reversed:", reversed_sentence)

print("-" * 50)
print("     STRING MANIPULATION COMPLETE!")
print("-" * 50)
