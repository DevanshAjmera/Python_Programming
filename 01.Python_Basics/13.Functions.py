#Function :- Block of statements that performs a specific task, and it can reuse anytime.

def printName():
    print("My function name is print .")
printName()

#function definition
def myAge(age):   # Parameter
    print("My age is ",age)
#function calling
myAge(18) # Argument


print("")
def areaSquare(side):
    print("My function name is areaSquare :",side*side)        # return 

area = int(input("Enter the square side: "))
#function calling
areaSquare(area)


"""
# Function to calculate average of 3 numbers
def average(a,b,c):
    return (a+b+c)/3

print(average(10,20,30))
#delivery cost, food cost, VAT, discount ......

# Default parameter :- If we do not pass any value to the parameter, then it will take the default value.
def areaCircle(radius, pi=3.14):  # Default parameter
    return pi*radius*radius

print(areaCircle(5,3.1)) # Default parameter
"""