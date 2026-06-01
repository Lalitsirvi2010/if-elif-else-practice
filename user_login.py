correct_username = "admin"
correct_password = "1234"
username_by_user = (input("Enter the username"))
password_by_user = (input("Enter password"))
if correct_password == password_by_user and correct_username == username_by_user:
    print("Login successful")
elif correct_password == password_by_user and correct_username != username_by_user:
    print("WRONG USERNAME")
elif correct_password != password_by_user and correct_username == username_by_user:
    print("WRONG PASSWORD")
else :
    print("Login failed")