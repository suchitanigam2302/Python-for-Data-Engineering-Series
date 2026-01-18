#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.

X = 1          #Integer Variable
X= "Suchi"   #String Variable
print(X)

name = "Suchita"
language = "Python"

print("My name is",name)
print(name,"Suchita is learning",language)
print(language,"is aewsome!")

#Casting        specify the data type of a variable
x= int(2)
y= str(3)
z= float(4)

print(x,y,z)

#the Type function
x = 5
y = "Data Engoneering"

print(type(x))
print(type(y))

#ASSIGN MULTIPLE VALUES TO MULTIPLE VARIABLES
a,b,c = "Python","is","Great"
print(a)
print(b)        
print(c)


#One Value to Multiple Variables
a=b=c="Python"
print(a)        
print(b)        
print(c)    


#UNPACKING A COLLECTION
fruits = ["Apple","Banana","Cheery"]
x,y,z=fruits
print(x)        
print(y)                
print(z)