#program to take a student name and roll number , then generate a username using the first 3 letter of the name and the last 2 digit of the roll Number 
name = input("Enter the student name :")
roll_no = input("Enter the roll number of the student ")
username = name[:3] + roll_no[-2:]
print(username)