# Write a python program to take total minutes as input and convert it into hours and remaining minutes 
total_min = int(input("Enter Total Minutes: "))

hours = total_min // 60
mintues = total_min % 60

print("Hours :",hours)
print("Remaining minutes:",mintues)