# 1. Write a python program to reverse a number using a while loop.

N = int(input("Enter Number: "))
rev = 0

while N > 0:
    digit = N % 10
    rev = (rev * 10) + digit
    N = N // 10
print(rev)
