# Q4 Age Calculator - Super Simple

print("AGE CALCULATOR")
print("==============")

# Get birth year
birth = int(input("What year were you born? "))
current = int(input("What year is it now? "))

# Calculate
age = current - birth
months = age * 12
days = age * 365
hours = days * 24
minutes = hours * 60
to_100 = 100 - age

# Show results
print("\n----- YOUR AGE -----")
print("Years:", age)
print("Months:", months)
print("Days (approx):", days)
print("Hours (approx):", hours)
print("Minutes (approx):", minutes)

if to_100 > 0:
    print("Years until 100:", to_100)
else:
    print("You are already 100+!")

print("==================")