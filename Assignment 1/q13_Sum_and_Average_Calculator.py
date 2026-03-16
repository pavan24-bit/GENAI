# Q13 Sum and Average 
print("SUM AND AVERAGE CALCULATOR")
print("==========================")

n = int(input("How many numbers? "))

total = 0
max_num = None
min_num = None

for i in range(n):
    num = float(input(f"Number {i+1}: "))
    
    # Add to total
    total = total + num
    
    # Check for max
    if i == 0 or num > max_num:
        max_num = num
    
    # Check for min
    if i == 0 or num < min_num:
        min_num = num

# Calculate average
avg = total / n

# Show results
print("\n===== RESULTS =====")
print(f"Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
print("===================")