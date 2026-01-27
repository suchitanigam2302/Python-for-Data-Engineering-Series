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


