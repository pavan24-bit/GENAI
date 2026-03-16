# Q5 Bill Splitter 
print("BILL SPLITTER")
print("=============")

# Get inputs
bill = float(input("Total bill: ₹"))
people = int(input("Number of people: "))
tax = float(input("Tax %: "))
tip = float(input("Tip %: "))

# Calculate
tax_amt = (tax / 100) * bill
after_tax = bill + tax_amt
tip_amt = (tip / 100) * after_tax
total = after_tax + tip_amt
each = total / people

# Show results
print("\n===== BILL DETAILS =====")
print(f"Subtotal: ₹{bill:.2f}")
print(f"Tax ({tax}%): ₹{tax_amt:.2f}")
print(f"After tax: ₹{after_tax:.2f}")
print(f"Tip ({tip}%): ₹{tip_amt:.2f}")
print(f"Total: ₹{total:.2f}")
print(f"Per person: ₹{each:.2f}")
print("========================")