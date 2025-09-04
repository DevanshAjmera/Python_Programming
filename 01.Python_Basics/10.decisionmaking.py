
"""# We have to use if else condition for decision making in python...
#Check you are eligible for voting or not. 
#Get the age from user
userAge=int(input("Enter your age: "))
#To check the user is eligible for voting, then check age must be greater than 18.

if userAge > 18:
     print("You are eligible for voting...")
else:
     print("you're not eligible for voting.")
"""



#Check the user is eligible for vote and Super vote
#Supervote age should be greater than and equals to 55.
#Vote age should be greater than equals to 18 and less than 55
userAge=int(input("Enter your age: "))
if (userAge >= 18 and userAge < 55):
    print("You are eligible for voting.")
elif (userAge >= 55):
    print("You are eligible for Super vote")
else:
    print("You are not eligible for voting.")



#To check traffic light colour and print message....
light = input("Enter the color: ")
if(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Look")
elif(light=="green"):
    print("Go")
else:
    print("You entered wrong light color !!")



#To check marks and give grades....
marks=int(input("Enter marks: "))
if (marks >= 90):
    print("A grade")
elif(marks >= 80 and marks <=89):
    print("B grade")
elif(marks >= 70 and marks <= 79):
    print("C grade")
else:
    print("D grade")



# Ternary Operator or Single line if condition
marks = int(input("Enter marks: "))
result = "Pass" if (marks >= 50) else "Fail"
print("Result is",result)
print("Pass") if (marks >=50 and marks <=100) else print("Fail")


#CLEVER IF 
age = int(input("Enter age : "))
vote = ("no","yes") [age>=18]  # if true (false_condition , true_condition)
print(vote)