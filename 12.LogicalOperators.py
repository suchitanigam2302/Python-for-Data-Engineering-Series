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