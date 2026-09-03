#write a program to take string and separate characters present at even index positions and odd positions 
string = input("Enter the string :")
even_character = string[::2]
odd_character = string[ :2]
print(even_character)
print(odd_character)