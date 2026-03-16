# Q12 Multiplication Table 

print("MULTIPLICATION TABLE")
print("====================")

n = int(input("Enter number: "))
r = int(input("Enter range: "))

print(f"\nTable of {n}:")
print("-" * 20)

for i in range(1, r+1):
    print(f"{n} x {i} = {n*i}")

print("-" * 20)