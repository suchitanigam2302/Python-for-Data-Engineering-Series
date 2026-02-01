#FOR LOOP
for item in range (1,5) :
    print(f"Rounds : {item}")

#Sequences
string = "Python"
for str in string :
    print(f"Sequences : {str}")

#Use Case 1
scores = [60,40,20,30]
total = 0
for score in scores :
    total += score
    print("Current total :",total)
print("Final Total :",total)