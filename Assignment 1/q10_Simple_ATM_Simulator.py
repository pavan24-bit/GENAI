# Q10 ATM Simulator 

balance = 10000
min_bal = 500

print("ATM SIMULATOR")
print("==============")

while True:
    print("\nMENU:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    ch = int(input("Choice: "))
    
    if ch == 1:
        print("Balance: ₹", balance)
        
    elif ch == 2:
        amt = float(input("Deposit amount: ₹"))
        if amt > 0:
            balance = balance + amt
            print("Deposit successful!")
            print("New balance: ₹", balance)
        else:
            print("Invalid amount!")
            
    elif ch == 3:
        amt = float(input("Withdraw amount: ₹"))
        if amt <= 0:
            print("Invalid amount!")
        elif (balance - amt) < min_bal:
            print("Insufficient balance!")
            print("Minimum balance ₹500 required")
        else:
            balance = balance - amt
            print("Withdrawal successful!")
            print("New balance: ₹", balance)
            
    elif ch == 4:
        print("Thank you!")
        break
        
    else:
        print("Invalid choice!")