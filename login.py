"""
Mini Project: Login System + Attempt Limit

Build a program that:

Checks username & password
Gives 3 attempts max
Prints success or locks user out

"""


def login(): 
    correct_username = "admin" 
    correct_password = "1234" 
    attempts = 3

    for i in range(attempts):
        username = input("Enter the Username: ") 
        password = input("Enter the password: ")
        if username == correct_username and password == correct_password: 
            print("user logged in successfully.")
            return
        else:
            print(f"Wrong Username or Password. you have {attempts - i -1} attempts left. Try again.")      
    print("Access denied Please try again later.")


login()