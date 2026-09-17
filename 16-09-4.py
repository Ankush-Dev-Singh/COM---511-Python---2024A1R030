#WAP a python program to input numbers in a list and find the second largest number 
n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("Second largest number =", second_largest)