#Repeatedly calculate the sum of digits until the result is a single digit

num = int(input("Enter a number: "))

while num >= 10:
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    num = total

print("Single digit result:", num)