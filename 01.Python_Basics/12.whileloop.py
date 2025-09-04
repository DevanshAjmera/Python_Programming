# While loop is used to perform iteration until condition will false
"""
#print the no from 1 to 10 using while loop
x=1
while x < 11:
    print(x)
    x=x+1
print(" ")

#WAP to print the no from 10 to 1 using while loop
y = 10
while y > 0:
    print(y)
    y=y-1
print(" ")


# #WAP to print the pattern using while loop  1,3,5,9,11
# a=1
# while a < 12:
#     if a == 7 :
#         print()
#     else:
#         print(a)
#         a = a+2

a=1
while a < 12:
    if a !=7 and a % 2 == 1:   #a % 2 != 0:
        print(a)
    a = a + 1
"""


# Program to find sum of first n numbers
i = 0
sum = 0
n = 7
while i <= n:
    sum+=i
    i+=1
print("Sum of first",n,"is",sum)



#Break :- Used to terminate the loop when encountered.

# To check a number in tuple using while loop...
j = 0
a = 16
b = 0
tup = (1,4,9,16,25,36,49,64,81,100)
while (j <len(tup)):
    b = (0,1) [tup[j] == a]
    if(b==1):
        break
    j+=1
print("Found") if (b==1) else print("Not Found")

# OR
j = 0
while (j <len(tup)):
    if (tup[j] == 10):
        print("Found")
        break
    j+=1
else:
    print("Not found")


"""
# Continue :- terminates execution in the current iteration & continues
#             execution of loop with next iteration.
# WAP to print the pattern using while loop  1,3,5,9,11
i = 1
while i <= 11 :
    if(i == 7):
        i += 2
        continue
    print(i)
    i += 2
"""
