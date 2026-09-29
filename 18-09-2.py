# 2. Store all month names in a tuple and input month number
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

n = int(input("Enter month number: "))

if 1 <= n <= 12:
    print("Month:", months[n - 1])
else:
    print("Invalid month number")