#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType 

a = 10      #int
b= "Hello" #str
c = 'Hi'   #str
d = True   #bool
e = False  #bool
f = None   #NoneType
g = ""     #str - blank
h = " "    #str - Empty space
j = "1234" #str - numbers in string
k = 12.34  #float
x=range(10) #range 
print(x)
print(list(x))
y=["apple","banana","cherry"]  #list
z=("apple","bannana","cheery") #tuple
m={"name":"Suchita","age":19} #dict
n={"apple","banana","cherry"} #set
o=frozenset({"apple","banana","cherry"}) #frozenset
p= b"Hello" #bytes - immutable sequence of bytes
q= bytearray(5)   #mutable sequence of bytes 
r= memoryview(bytes(5)) #Data ki copy banaye bina direct memory access deta hai



#PYTHON CHALLENGE
age = 19
height = 180.34 
name = "Suchita"
Are_you_a_student = True
result = None

print("Age:",age)
print(type(age))
print(age.bit_length())

print("Height:",height)
print(type(height))


print("Name:",name)
print(type(name))
print(len(name))
print(name.upper())

print("Are You a Student:",Are_you_a_student)
print(type(Are_you_a_student))

print("Result:",result)
print(type(result))