# 1. Python program to check leap year  or not.

year = int(input("Enter a year: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is a leap year." if leap_year else f"{year} is not a leap year.")
