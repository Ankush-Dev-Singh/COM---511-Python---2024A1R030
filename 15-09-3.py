#Write a python program to print a right angled triangle using stars 
# *
# * * 
# * * * 
# * * * *
n = int(input("Enter the number of rows :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()     
    