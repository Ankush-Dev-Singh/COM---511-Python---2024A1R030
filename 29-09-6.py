#Write a ppython program to create records of n students. Store each student record as n students .Store 
# each student record as a dictionary containing roll.number name,branch and marks . Store all records in a list and
# search for the student using roll number.(Condition. Roll number must be unique)

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    while True:
        roll = input("Enter roll number: ")

        # Check whether roll number already exists
        if any(student["roll"] == roll for student in students):
            print("Roll number already exists. Enter a different roll number.")
        else:
            break

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

# Display all student records
print("\nStudent Records:")

for student in students:
    print(student)

# Search student using roll number
search_roll = input("\nEnter roll number to search: ")

found = False

for student in students:
    if student["roll"] == search_roll:
        print("\nStudent Found:")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student not found.")