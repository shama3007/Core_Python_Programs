# 2. Write a Python program to get the largest and smallest number from a list without built in functions.


def find_largest_smallest(numbers):
    if not numbers:
        return None, None

    smallest = largest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return smallest, largest


numbers = [3, 1, 7, 0, -2, 8, 5]
smallest, largest = find_largest_smallest(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
