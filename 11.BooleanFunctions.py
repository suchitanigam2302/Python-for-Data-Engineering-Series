#Boolean Functions
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))


email = "suchi@gmail.com"
phone = "09808098"
username = "suchi23"

#allows registration if any field is filled
print(any([email,phone,username]))

#allows registration if all the fiels are filled
print(all([email,phone,username]))

print(isinstance(123,int))
print(isinstance(True,str))

print("Hello".endswith("o"))
print("Hello".startswith("o"))