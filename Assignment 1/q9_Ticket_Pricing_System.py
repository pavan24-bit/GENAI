# Q9 Ticket Pricing 

print("MOVIE TICKET PRICE CALCULATOR")
print("==============================")

# Get inputs
age = int(input("Your age: "))
day = input("Day (Monday-Sunday): ").lower()
tickets = int(input("Number of tickets: "))

# Base price based on age
if age < 3:
    price = 0
    cat = "Free"
elif age <= 12:
    price = 150
    cat = "Child"
elif age <= 59:
    price = 300
    cat = "Adult"
else:
    price = 200
    cat = "Senior"

# Check discount (weekend)
if day == "friday" or day == "saturday" or day == "sunday":
    discount = 20
else:
    discount = 0

# Calculate
base_total = price * tickets
discount_amt = (discount / 100) * base_total
final = base_total - discount_amt

# Show results
print("\n===== TICKET SUMMARY =====")
print("Category:", cat)
print("Price per ticket: ₹", price)
print("Tickets:", tickets)
print("Base total: ₹", base_total)

if discount > 0:
    print("Discount:", discount, "%")
    print("You save: ₹", discount_amt)

print("FINAL TOTAL: ₹", final)
print("==========================")