# 2. Declare two variables and print that which variable is largest using ternary operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = a if a > b else b
print(f"The largest number is: {largest}")
