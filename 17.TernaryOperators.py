score = 100
# if score >= 90:
#       print("A")
#elif score >= 80:
#       print("B")
#else:
#       print("F")

#if else one line 
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)


country = "India"
if country == "United States":
        print("US")
elif country == "India":
        print("IN")
elif country == "Germany":
        print("DE")
elif country == "Egypt":
        print("EG")
else :
        print("Unkown Country")

#match case
match country :
        case "United States" | "USA" :
            print("US")
        case "India":
              print("IN")
        case "Germany":
              print("GE")
        case "Egypt":
              print("EG")
        case _:
              print("Unknown Country")