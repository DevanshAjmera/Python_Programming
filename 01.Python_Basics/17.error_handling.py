"""
#print(x)    #NameError: name 'x' is not defined
try:
   print(x)
except NameError:
    print("name x is not defined")
"""


# y=1/0
# print(y)          #ZeroDivisionError: division by zero
try: 
    y=1/0
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")



try:
    a="Pawan"
    b=int(a)
    print(b)
except ValueError: 
    print("ValueError: invalid literal for int() 'Pawan'")


try:
    import os
    os.remove("myfile.txt")
except FileNotFoundError:
    print("FileNotFoundError: The system cannot find the file specified: 'myfile.txt'")


mylist=["pawan","Devansh","Prince"]
try: 
    print(mylist[4])
except IndexError:
    print("SyntaxError: index not found")




x=5
# if x>5:
#     print(x)
# else:
#     print(x)
try:
    if x>5:
        print(x)
    else:
        print(x)
except IndentationError :
    print("IndentationError: expected an indented block after 'if'")




try:
    x="Pawan"
    y=4
    c=x+y
    print(c)
except TypeError:
    print("TypeError: can only concatenate str to str")
finally:
    print("always run")