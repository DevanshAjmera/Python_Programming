# Search for a number in tuple using for loop
tup = (1,4,9,16,25,36,49,64,81,100)
for search in tup:
    if (search == 10):
        print("Found")
        break
else:
    print("Not found")

# Range :- range(start? -> 0 by default, stop, step? -> 1 by default) 
# Print sequence (1,3,5,9,11)
for i in range(1,12,2 ):
    if(i != 7):
        print(i)

# Print the table of number.
n = 7
for i in range(0,10*n+1,n):
    print(i)

# pass :- is a null statement that does nothing. It is used as a placeholder for future code.
for el in range(10):
    pass  # used in try, catch



# Program to print Factorial of first n numbers.
n = 5
fact = 1 
for i in range(1,n+1,1):
    fact*=i
print("Factorial is ",fact)

