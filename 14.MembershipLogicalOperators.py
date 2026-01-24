print("f" in "python")
print("f" not in "python")


print("o" in "python")
print("o" not in "python")

print (3 in [1,2,3])

#Security Checks : ensure the domain is not banned

domain = input("Emter the domain:" )
is_banned = ["spam.com","fake.org","bot.net"]
print(domain not in is_banned)