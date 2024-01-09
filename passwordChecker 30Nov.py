import re

def is_password_strong(password):
    #Password complexity rules
    min_length = 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    # Check against complexity rules

    #check against complexity rules
    if len(password) < min_length:
        return False, "Password should be atleast 8 characters long."
    if not has_uppercase:
        return False, "Password should contain atlest one uppercase letter."
    if not has_lowercase:
        return False, "Password should contain at least one lowercase letter."
    if not has_digit:
        return False, "Password should contain at least one digit."
    
    return True, "Password meets all the complexity requirements"

#Get user input and save the password data
while True:
    password = input("Enter your password: ")
    result, messege = is_password_strong(password)
    if result:
        print("Password is Srtong. Saving password data..")
        #Here you can save password to a file or  database.the actual way of saving the password could vary based on the specific use
        break
    else:print(messege)
    print("please try again")

print("Password data saved successfully.")
