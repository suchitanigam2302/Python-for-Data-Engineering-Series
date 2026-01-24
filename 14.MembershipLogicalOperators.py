print("f" in "python")
print("f" not in "python")


print("o" in "python")
print("o" not in "python")

print (3 in [1,2,3])

#Security Checks : ensure the domain is not banned

domain = input("Emter the domain:" )
is_banned = ["spam.com","fake.org","bot.net"]
print(domain not in is_banned)

#Identity Operator

x = ['a','b','c']
y = ['a','b','c']   # y= x points to the same location = True 

print(x==y)
print(x is y)

a = 10
b =10
print(a == b)
print(a is b)

#Make Sure the email exists,and it not empty

email  = input("Enter your email:" )
print(email is not None and email != "")