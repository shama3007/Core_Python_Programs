# 2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .


def square(num):
    return num**2


number = int(input("Enter Number: "))
result = square(number)
print(f"The square of {number} is {result}")
