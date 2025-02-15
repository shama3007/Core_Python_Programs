# 3. Write a python program finding the factorial of a given number using a while loop.


def FactorialNo(N: int):
    res = 1
    if N < 0:
        print("Factorial of No is Negative")
    while N > 0:
        res *= N
        N -= 1
    return res


a = int(input("Enter Number: "))
print(FactorialNo(a))
