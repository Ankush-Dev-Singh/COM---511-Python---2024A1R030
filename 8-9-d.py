#Write a Python program to create a simple password validation system
#the program should repeatedly ask the user to eneter a password until a valid password is entered
#A password will considered valid only if it has at least 8 character and contains @ symbol 
#once rhe user eneters a vlaid password the program should display, password accpeted and stop ,otherwise it should display " Weak password . Try again"
# and ask for password again 
while True:
    password = input("Enter your password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted")
        break
    else:
        print("Weak password. Try again")