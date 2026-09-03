# Q3 To take the an amount in rupees and calculate how many 500 and 100 notes are needed 
# Exam :3800 = 7 notes of 500 and 3 notes of 100

amount = int(input("Eneter the total amount "))
notes_500 = amount //500
remaining = amount % 500

notes_100 = remaining //100
remain = amount % 10 

print("500 Notes : ",notes_500)
print("100 Notes : ",notes_100)