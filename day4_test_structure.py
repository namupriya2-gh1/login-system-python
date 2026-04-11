# Login function (Logic layer)
def login(username, password):
    if username == "admin" and password == "1234":
        return "PASS"
    elif username == "":
        return "INVALID INPUT"
    else:
        return "FAIL"
    

#Test data (Data layer) 
test_users = [("admin", "1234", "PASS"),
    ("admin", "wrong", "FAIL"),
    ("user", "wrong", "FAIL"),
    ("guest", "1234", "FAIL"),("","", "FAIL")
]

#Test execution (Test layer)
def test_login():
    for username, password, expected in test_users:
        result = login(username, password)

        if result == expected:
            print(f"✅ pass: {username} | Expected: {expected}, Got: {result}")
        else:
            print(f"❌ fail: {username} | Expected: {expected}, Got: {result}")

#Run test
test_login()
