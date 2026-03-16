# Q20 Number Functions 

def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "No factorial for negative"
    ans = 1
    for i in range(1, n + 1): 
        ans = ans * i
    return ans

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True 

def sum_of_digits(n):
    """Add all digits of a number"""
    n = abs(n)
    total = 0
    for digit in str(n):
        total = total + int(digit)
    return total  

def reverse_number(n):
    """Reverse the digits of a number"""
    if n < 0:
        n = abs(n)
        return -int(str(n)[::-1])  
    else:
        return int(str(n)[::-1])  

def gcd(a, b):
    """Find Greatest Common Divisor"""
    a = abs(a)
    b = abs(b)
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

def lcm(a, b):
    """Find Least Common Multiple"""
    a = abs(a)
    b = abs(b)
    bigger = max(a, b)
    i = bigger
    while True:
        if i % a == 0 and i % b == 0:
            return i
        i = i + bigger 

# Main menu
print("=" * 50)
print("     NUMBER FUNCTIONS PROGRAM")
print("=" * 50)
print()
print("Choose a function:")
print("-" * 40)
print("1. Factorial")
print("2. Check Prime")
print("3. Sum of Digits")
print("4. Reverse Number")
print("5. GCD (Greatest Common Divisor)")
print("6. LCM (Least Common Multiple)")
print("7. Exit")
print("-" * 40)

while True:
    print()
    choice = input("Enter your choice (1-7): ")
    
    if choice == "7":
        print()
        print("=" * 40)
        print("Thanks for using the program!")
        print("Goodbye!")
        print("=" * 40)
        break
    
    elif choice == "1":
        print()
        n = int(input("Enter a number: "))
        result = factorial(n)
        print(f"{n}! = {result}")
    
    elif choice == "2":
        print()
        n = int(input("Enter a number: "))
        if is_prime(n):
            print(f"{n} is a PRIME number")
        else:
            print(f"{n} is NOT a prime number")
    
    elif choice == "3":
        print()
        n = int(input("Enter a number: "))
        result = sum_of_digits(n)
        print(f"Sum of digits of {n} = {result}")
    
    elif choice == "4":
        print()
        n = int(input("Enter a number: "))
        result = reverse_number(n)
        print(f"Reverse of {n} = {result}")
    
    elif choice == "5":
        print()
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = gcd(a, b)
        print(f"GCD of {a} and {b} = {result}")
    
    elif choice == "6":
        print()
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = lcm(a, b)
        print(f"LCM of {a} and {b} = {result}")
    
    else:
        print(" Invalid choice! Please enter 1-7 only.")
    
    print("-" * 30)