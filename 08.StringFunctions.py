#Types Functions in Python

name = "Suchita"
print(type(name))

age = 19
print(type(age))
print("Your Age is:" + str(age))

#Math Functions
#1.length function
password = input("Enter your password:")
print(len(password))

if(len(password)<8):
    print("Password is too short")
else:
    print("Password is correct")


#2.Count function
message = '''I'm Learning Python
Python is very powerful language
Python is used in many applications'''

print(message.count("is"))

#Transformations Functions
#1.Replace function
price = "$1,233.99"
print(price.replace("$","").replace(",",""))

price1 = "+49 (176) 123-4567"
print(price1.replace("(","").replace(")","").replace("-","").replace(" ","").replace("+","00"))

#2.Concatenation function
First_name = "Suchita"
Last_name = "Nigam"
Last_name1=First_name + " " + Last_name
print(Last_name1)

folder = "C:/Users/Suchita/"
file = "data.csv"
full_file_path = folder + file
print(full_file_path)

#f"String"
name = "Suchita"
age = 19
is_student  = False
print("My name is " + name + ",I am " + str(age) + "years old")
print(f"My name is {name},I am {age} years old")

print(f"2 + 3  = {2+3}")

print(f"{{This is me}}")

#4.Spilt function

stampe = "Dear Suchita,Your order has been shipped and will be delivered to you soon.Thank you for shopping with us."
print(stampe.split(","))

stamp = "2026-08-15 14:30"
print(stamp.split("-"))

csv_file = "name,age,city,country"
print(csv_file.split(","))