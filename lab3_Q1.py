# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.


def div(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = div(a, b)
print(f"Division result: {result}")
