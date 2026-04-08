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