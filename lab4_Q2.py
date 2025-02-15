# 2. Write a python program to check whether a number is palindrome or not?


def PalindromeNo(N: int):
    if str(N) == str(N)[::-1]:
        return f"{N} is palindrome"
    else:
        return f"{N} is not palindrome"


a = int(input("Enter Number: "))
print(PalindromeNo(a))
