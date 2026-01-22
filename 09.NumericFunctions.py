#Type Functions
x =10
y = 3
z =2 + 3j

print("Value of x:",x)
print("Type of x:",type(x))
print("Value of y:",y)
print("Type of y:",type(y))
print("Value of z:",z)
print("Type of z:",type(z))

#Integer Conversion
a = "24"
print(type(a))
print(a * 3)
b = int(a)
print(type(b))
print( b * 3)


#Float Conversion
c = "3.14"
print(float(c))

#Complex Number

d = 3 #real part
e = 4 #imaginary part
print(complex(d,e))

#Math Operators
print (2 + 3)    # Addition
print (5 - 2)    # Subtraction
print (4 * 3)    # Multiplication
print (10 / 2)   # Division
print (10 // 3)  # Floor Division
print (10 % 3)   # Modulus
print (2 ** 3)   # Exponentiation

x1 = 2
x1 = x1 + 3
x1 += 3
print(x1)

x1-= 1
print(x1)

x *= 2
print(x)

#Rounding Nukbers
import math
price = 19.99
print(round(price))
print(round(price,2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

#Random Functions
import random
print(random.random())
print(random.randint(1,10))

#Validation Function
#1.is_integer()
f = 7.0
print(f.is_integer())

g = 7.8
print(g.is_integer())

#2.isinstance()
h = 10.2
print(isinstance(h,int))
print(isinstance(h,float))

#Advanced Math FUnctions

import math

i = 2
print(math.sqrt(i))  # Square root of x
print(math.sin(i))  # Sine of x
print(math.cos(i))  #Cosine of x
print(math.log(i))  # Natural logarithm of x
print(math.factorial(i))  # Factorial of x