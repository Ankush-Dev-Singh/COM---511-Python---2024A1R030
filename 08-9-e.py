#Write a program to input marks of 5 students 
#For each student the program should check wheather the entered marks are valid or invalid .Marks
# are considered valid only it they are between 0 and 100,if the marks are invalid the program should display 
#"invalid marks skipped " and move to the next students without printing those marks
# if the marks are valid the program should display the marks as valid
for i in range(1, 6):
    marks = int(input("Enter marks of student: "))

    if marks >= 0 and marks <= 100:
        print("Valid marks:", marks)
    else:
        print("Invalid marks skipped")
        