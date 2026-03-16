# Q2 assignment

print("WELCOME TO CALCULATOR")
print("--------------------")

# Getting numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nRESULTS:")
print("---------")

# Addition
print(a, "+", b, "=", a + b)

# Subtraction
print(a, "-", b, "=", a - b)

# Multiplication
print(a, "x", b, "=", a * b)

# Division
print(a, "/", b, "=", round(a / b, 2))

#Floor Division
print(a, "//", b, "=", round(a // b, 2))

# Modulus
print(a, "%", b, "=", a % b)

# Exponentiation
print(a, "^", b, "=", a ** b)

print("---------")
print("DONE!")