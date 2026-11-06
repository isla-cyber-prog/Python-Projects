print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = input("Choose an option: ")

if choice == "1":
    celsius = float(input("Enter Celsius: "))
    print(f"{(celsius * 9/5) + 32:.1f}°F")

elif choice == "2":
    fahrenheit = float(input("Enter Fahrenheit: "))
    print(f"{(fahrenheit - 32) * 5/9:.1f}°C")

elif choice == "3":
    celsius = float(input("Enter Celsius: "))
    print(f"{celsius + 273.15:.2f}K")

else:
    print("Invalid option.")
