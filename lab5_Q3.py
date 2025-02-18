# 3. Write a Python program to find duplicate values from a list and display those.


def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1, 9, 10, 5]
print("Duplicate values:", find_duplicates(numbers))
