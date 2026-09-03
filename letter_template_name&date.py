#Write a program to fill the given the letter template with name and date 
letter = '''
Dear <Name>,
You are selected
<Date>
'''
name = input("Enter name: ")
date = input("Enter date: ")

letter = letter.replace("<Name>,name")
letter = letter.replace("<Date>",date)

print(letter)