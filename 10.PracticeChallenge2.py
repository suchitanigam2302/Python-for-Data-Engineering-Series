#Create a program that asks the user for their name and age, then prints a formatted greeting message.

#Taking input
name = input("Name :")
age = int(input("Age :"))

#Greeting Message using f string
print(f"Hello {name}! You are {age} years old.")

# Create a program that asks the user for a word and prints:
#The word in uppercase
#The word in lowercase
#The length of the word

word = input("Enter any random Word :")
print("Uppercase:",word.upper())
print("Lowercase:",word.lower())
print("Length:",len(word))

#🧩 Challenge 3 (Medium – Combines Multiple Concepts)
#Create a program that:
#Takes a sentence from the user
#Prints:
#Total number of characters
#Sentence in uppercase
#Sentence with spaces replaced by _

sentence = input("Enter any sentence as per your choice:")
print("Characters:",len(sentence))
print("Upeercase:",sentence.upper())
print("Modified:",sentence.replace(" ","_"))

#Create a program that:
#Takes two numbers from the user
#Prints:
#Their sum
#Their difference
#Their product

number1 = int(input("Enter Number 1: ")) #can be done with float and its better approach
number2 = int(input("Enter Number 2: "))
print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)

#Create a program that:
#Takes a price and a discount percentage
#Calculates and prints the final price after discount

price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)

#Create a program that:
#Takes user’s name and year of birth
#Calculates their age (assume current year = 2025)

fullname = input("Enter your name: ")
dob = int(input("Enter your Date Of Birth: "))

age = 2025 - dob

print(f"Hello {fullname}, you are {age} years old")

#Create a program that:
#Takes a string containing a number (example: "45.67")
#Converts it into a float
#Prints:
#Rounded value (use round())
#Integer value (use int())

number3 = input("Enter a string containing a number: ")
num = float(number3)
print("Rounded:", round(num))
print("Integer:", int(num))

#Create a program that:
#Takes a sentence
#Prints:
#Total characters
#Total words
#Sentence with first letter capitalized (capitalize())