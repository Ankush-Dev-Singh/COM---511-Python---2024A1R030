#Write a python student full name and roll number.Generate email using first 3 letters of first name 
#,first 3 letter of last name,and last 3 character of roll number 
first_name = input("Enter the first name :")
last_name = input("Enter the last name :")
roll_no = input("Enter the rollNo: ")
email = first_name[:3] + last_name[:3] + roll_no[-3:] + '@mietjammu.in'
print(email)