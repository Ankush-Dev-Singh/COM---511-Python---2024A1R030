#Write a python program to take the word  and count the number of vowels a,e,i,o,u
word = input("Enter the word :")
number = word.count('a') + word.count('e') + word.count('i') + word.count('o')+ word.count('u')
print(number)