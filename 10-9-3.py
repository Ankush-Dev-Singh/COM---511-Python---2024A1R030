#take  the input of decimal  number and convert it into binary number without built in bin() functionnum = int(input("Enter a number: "))
num = int(input("Enter the decimal number :"))
binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary =", binary)