# 3. Python Program to Check if a Number is Positive, Negative or zero

num = int(input("Enter a number: "))
status = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
print(f"The number {num} is {status}.")
