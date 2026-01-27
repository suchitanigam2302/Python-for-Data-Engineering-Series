#if statement
score = int(input("Enter the score:" ))
is_project_submitted = True
if score >= 90 and is_project_submitted: #Logical operators
    print("A+")
elif score >=90 :
       print("A")
#elif
elif score >= 80:
        print("B")
#Multi elif
elif score >= 70:
        print("C")

elif score >= 60 and is_project_submitted:
        print("D")

elif score >= 50:
        print("E")
# else
else:
        print("F")



#Independent if
if score >= 90 :
       print("High Score")
else :
       print("Low Score")

if is_project_submitted :
       print("Project is Submitted")
else :
       print("Project is not Submitted")

#ABove all are conditional statements
