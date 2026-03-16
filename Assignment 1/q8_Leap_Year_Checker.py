# Question 8: Leap Year Checker 

print("=" * 50)
print("     LEAP YEAR CHECKER")
print("=" * 50)
print()

try:
    year = int(input("Enter a year: "))
    
    # Year is leap if: divisible by 4 AND (not divisible by 100 OR divisible by 400)
    is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    
    print("\n" + "-" * 50)
    
    if is_leap:
        print(f" {year} is a LEAP YEAR!")
        print(f"   Reason: It satisfies the leap year rules.")
    else:
        print(f" {year} is NOT a leap year!")
        
        # Give specific reason
        if year % 4 != 0:
            print(f"   Reason: {year} is not divisible by 4.")
        elif year % 100 == 0 and year % 400 != 0:
            print(f"   Reason: {year} is divisible by 100 but not by 400.")
    
    print("-" * 50)
    
except ValueError:
    print(" Please enter a valid year number.")
