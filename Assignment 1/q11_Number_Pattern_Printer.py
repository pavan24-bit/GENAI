# Q11 Pattern Printer -

print("PATTERN PRINTER")
print("===============")

p = int(input("Pattern (1-4): "))
h = int(input("Height: "))

if p == 1:
    # Pattern 1
    for i in range(1, h+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
        
elif p == 2:
    # Pattern 2
    for i in range(1, h+1):
        for j in range(1, i+1):
            print(i, end="")
        print()
        
elif p == 3:
    # Pattern 3
    for i in range(h, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()
        
elif p == 4:
    # Pattern 4
    for i in range(1, h+1):
        # Increasing
        for j in range(1, i+1):
            print(j, end="")
        # Decreasing
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()
        
else:
    print("Invalid pattern!")