# Q2 To take the two digit as input and print the sum of its digit

x = int(input("Enter the Two Digit "))
first_digit = x // 10
second_digit = x % 10

sum = first_digit + second_digit

print("Sum of its digits = ",sum)