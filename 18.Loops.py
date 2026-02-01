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

# 7 Table
for table in range (1,11):
    print(f"7 * {table} = {7 * table}")

for t in range (1,11):
    print(f"10 * {t} = {10 * t}")

star = "*"
for i in range (1,7):
    print (f"{star * i}")