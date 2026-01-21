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

#string * function

print ("ha" * 5)
print("-" * 20)

#5.Indexes and Slicing
text = "Python"

#Extracting the first letter
print(text[0])
print(text[-6])

#Extracting the last character
print(text[5])
print(text[-1])

#Exract h
print(text[4])
print(text[-3])

date = "2026-09-20"
print(date[0:4])
print(date[:4])

#Extract the month
print(date[5:7])

#Extract the day
print(date[8:])

#Cleaning Functions

#1.lstrinp() function
text = "   Hello Python".lstrip()
print(text)

#2.rstrip function
text1 = "Hello World  ".rstrip()
print(text1)

#strip function
text2 =  "  Hello Python  ".strip()
print(text2)

text3 = "***Hello World***".strip("*")
print(text3)

#Clean whitespaces 
messsage_with_spaces = "  Hi I,m Suchita"
print(len(messsage_with_spaces))
print(len(messsage_with_spaces.strip()))

no_of_spaces = len(messsage_with_spaces)-len(messsage_with_spaces.strip())
is_data_clean = len(messsage_with_spaces) == len(messsage_with_spaces.strip())

print("No of leading and trailing spaces:",no_of_spaces)
print("Is Data Clean:",is_data_clean)


#CaseConversion Functions

#1.lower() function
text5 = "data ENGINEERING"
print(text5.lower())
print(text5.upper())

Search = " Email".lower().strip()
data = "emaIl".lower().strip()

print(Search == data)

