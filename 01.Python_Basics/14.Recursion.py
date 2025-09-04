# RECURSION :- When a function calls itself repeatedly.
"""
def show(n):
    if(n == 0):   # Base case
        return
    print(n)
    show(n-1)
    print("End of recursion..")
    print(n)
show(5)
"""


"""
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n-1)
print("Factorial is",factorial(5))  


def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
print(sum(4))
"""


"""
list = [1,2,3,4,5,6,7,8,9,10]
def listprint(i = 0):
    if i == len(list):
        return 0
    print(list[i], end = " ")
    listprint(i+1)
listprint()    # print whole list
print("")
listprint(4)   # list from 5 to 10...
"""
