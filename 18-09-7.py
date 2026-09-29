# 7. Store multiple students as a list of tuples and display students scoring above 75
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))

    student = (name, roll, marks)
    students.append(student)

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print(student)