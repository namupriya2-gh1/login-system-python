#Login function

def login(User_name, Password):
    if User_name == "Namu" and Password == "1234":
        return "Success!"
    else:
        return "Failed"
    
    
result = login("Namu", "1234")
if result == "Success!":
    print("Test Passed")
else:
    print("Test Failed")


#User authentication function

def check_user_role(role):
    if role == "admin":
        print("Full access granted.")
    else:
        print("Limited access granted.")


check_user_role("admin")
check_user_role("guest")

#Reusable login function with multiple users

def user_login(username, password):
    if username == "admin" and password == "1234":
        return "success"
    else:
        return "fail"


users = [
    ("admin", "1234"),
    ("guest", "0000"),
    ("testuser", "1234")
]

for username, password in users:
    result = user_login(username, password)

    if result == "success":
        print("Testing user:", username, "Passed")
    else:
        print("Testing user:", username, "Failed")