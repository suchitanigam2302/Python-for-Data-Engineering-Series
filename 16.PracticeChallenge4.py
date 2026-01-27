#Email
email = input("Enter your email :")
#Clean the string
email = email.strip()
#email not be empty
if email == "" :
    print("Email cannot be empty")
#Email must contain . and @
elif not('.' in email and '@' in email):
    print("Email must contain . and @ ")
#Email must have only one @    
elif email.count('@') !=1 :
    print("Email only have one @")
#Email must cEND WITH '.'.'@' symbol
elif not email.endswith(('.com','org','.net')) :
    print("Email must end with by the above ")
#Email muat not be more than 254 charqcters
elif len(email) > 254 :
    print("Email must be more than 254 characters")
#Email must start with letter or digit
elif not(email[0].isalnum() and email[-1].isalnum()) :
    print("email must not start and end with letter or digit")
else :
    print("Email is valid")


#password

password = input("Enter password: ")
email = input("Enter email: ")

# Clean the password
password = password.strip()

# Password must not be empty
if password == "":
    print("Password should not be empty")

# Must be at least 8 characters
elif len(password) < 8:
    print("Password length should be at least 8 characters")

# Must include at least 1 uppercase letter
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter")

# Must include at least 1 lowercase letter
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter")

# Must not be same as email
elif password == email:
    print("Password should not be same as email")

# Password must start and end with letter or digit
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")

else:
    print("Password is correct ✅")
