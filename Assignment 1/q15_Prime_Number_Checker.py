# Q15 Prime Number Checker

print("PRIME NUMBER CHECKER")
print("====================")

# ===== PART 1: Check single number =====
print("\n--- PART 1: Single Number Check ---")
n = int(input("Enter a number: "))

# Check if prime
if n < 2:
    print(f"{n} is NOT prime (numbers less than 2 are not prime)")
elif n == 2:
    print(f"{n} is PRIME (2 is the only even prime)")
elif n % 2 == 0:
    print(f"{n} is NOT prime (even numbers >2 are not prime)")
else:
    # Check odd divisors
    is_prime = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            print(f"{n} is NOT prime (divisible by {i})")
            break
    
    if is_prime:
        print(f"{n} is PRIME")

# ===== PART 2: Find primes in range =====
print("\n--- PART 2: Find Primes in Range ---")
start = int(input("Enter start: "))
end = int(input("Enter end: "))

primes = []
for num in range(start, end + 1):
    if num < 2:
        continue
    
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)

print(f"\nPrime numbers from {start} to {end}:")
if primes:
    print(primes)
else:
    print("No primes found")