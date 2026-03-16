#Q18 Calculator 
print("SIMPLE CALCULATOR")
print("-" * 20)

# Get numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# division 
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Show results
print("\nRESULTS:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
print(f"{num1} ÷ {num2} = {division}")