#wap to checl whether a no is a perfect no.a no is perfect no if the sum of its proper divisor is equal tp no itself

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")