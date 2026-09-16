#Write a python program to print a sequare pattern of stars for  rows and n columns
# * * * *
# * * * *
# * * * *
# * * * *
n = int(input("Enter number of rows and columns: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
