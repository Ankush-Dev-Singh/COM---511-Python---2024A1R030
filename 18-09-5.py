# 5. Check whether a value is present and display its position

t = (10, 20, 30, 40, 50)
value = int(input("Enter value to search: "))
if value in t:
    print("Value found")
    print("Position:", t.index(value) + 1)
else:
    print("Value not found")