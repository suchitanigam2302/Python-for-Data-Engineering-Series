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

#Data Cleaning
files = [" Reprot.csv "," DATA.csv","final.TXT "]
for file in files:
    file = file.strip().lower().replace('txt','csv')
    print(f"Processing : {file}")