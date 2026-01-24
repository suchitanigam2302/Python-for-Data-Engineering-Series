#Logical Operators

#and operator---------both condition should be true
print(3 < 1 and 5 < 1)
print(3 > 1 and 5 > 1)

#or operator---------- at least one value should be true
print(3 > 1 or 5 < 1)
print(3 < 1 or 5 < 1)

#Checks if the system is under pressure
cpu_usage = 70
memory_usage = 50
print(cpu_usage < 90 or memory_usage > 90)
print(cpu_usage > 70 or memory_usage > 90)

#Checking user creditianls before kofim
email = True
password = False
print(email and password)

#Not Operator
print(not True)
print(not False)
print(not 3 > 1)
print(not not False)

name = "" 
print(not name)
print(not 0)  # 0 is already false and not 0 is true