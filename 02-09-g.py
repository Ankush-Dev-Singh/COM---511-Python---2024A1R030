#Write a program to take the password aand checks it contains @ and atleast 8 characters
password = input("Enter the password :")
if "@" in password and len(password) >= 8:
    print("Valid Password: ")
else:
    print("Invalid Password :")
