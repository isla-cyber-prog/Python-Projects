import math

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")

choice = input("Choose an option: ")

if choice == "5":
    num = float(input("Enter number: "))

    if num >= 0:

print(math.sqrt(num))
else: 
    print("cannot calculate the square root of a negative number.")
    print(f"Square root =
    {math.sqrt(num)}")
