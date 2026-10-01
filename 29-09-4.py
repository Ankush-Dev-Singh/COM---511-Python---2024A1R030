#Write a python program to perform searching activity using linear and binary search


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
key = int(input("Enter number to search: "))

# Linear Search
found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Linear Search: Element found at position", i + 1)
        found = True
        break

if not found:
    print("Linear Search: Element not found")


# Binary Search
numbers.sort()
print("Sorted list:", numbers)

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Binary Search: Element found at position", mid + 1)
        found = True
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Element not found")