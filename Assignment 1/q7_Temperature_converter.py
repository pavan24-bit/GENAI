# Q7 Temperature Converter 

print("TEMPERATURE CONVERTER")
print("=====================")
print("1. C to F")
print("2. F to C")
print("3. C to K")
print("4. K to C")
print("5. F to K")
print("6. K to F")
print("7. Exit")

choice = int(input("Choose (1-7): "))

if choice == 1:
    c = float(input("Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")
    
elif choice == 2:
    f = float(input("Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")
    
elif choice == 3:
    c = float(input("Celsius: "))
    k = c + 273.15
    print(f"{c}°C = {k}K")
    
elif choice == 4:
    k = float(input("Kelvin: "))
    c = k - 273.15
    print(f"{k}K = {c}°C")
    
elif choice == 5:
    f = float(input("Fahrenheit: "))
    k = (f - 32) * 5/9 + 273.15
    print(f"{f}°F = {k}K")
    
elif choice == 6:
    k = float(input("Kelvin: "))
    f = (k - 273.15) * 9/5 + 32
    print(f"{k}K = {f}°F")
    
else:
    print("Invalid choice!")