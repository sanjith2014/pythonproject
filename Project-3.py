password="scratch"
your_password=input("Enter the password:")
while your_password!=password:
    your_password=input("Wrong password,Enter the password again:")
else:
    print("Access Granted")