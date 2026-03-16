# q16 Number Guessing Game

import random

print("GUESS THE NUMBER GAME")
print("=" * 30)

# Computer picks a number
secret = random.randint(1, 100)
attempts = 7

print("I picked a number from 1 to 100")
print(f"You have {attempts} tries")

# Loop for 7 attempts
for attempt in range(1, 8):
    print(f"\nAttempt {attempt} of 7")
    
    # Get guess
    guess = int(input("Your guess: "))
    
    # Check guess
    if guess == secret:
        print("\nYOU WIN! 🏆")
        print(f"Correct! The number was {secret}")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
    
    if attempt == 7:
        print("\nGAME OVER!")
        print(f"The number was {secret}")

print("\nThanks for playing!")