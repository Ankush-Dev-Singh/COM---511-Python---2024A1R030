#code to mask the mobile number 
mobile = input("Enter the mobile number :")
masked = "******" + mobile[-4:]
print("Masked mobile number =",masked)