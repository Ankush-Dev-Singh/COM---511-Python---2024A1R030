#Write a program to print the centered pyramid using stars
#    *
#   * *
# * * * * *
#* * * * * * *


n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")

    print()
