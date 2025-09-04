# type: ignore
str1 = "Apple"
str2 = "Orange"
print(str1)
print(len(str1))
print(str2)
print(len(str2))
print(str1 +" and "+ str2)
print(str1[:-2])


str = "i am a coder"
a=str.endswith("er")   #returns true if string ends with substring
b=str.capitalize()     #capitalize 1st char
c=str.replace("a","A") #replaces all occurrences of old with new
d=str.find("a")       #returns 1st index of 1st occurrence
e=str.count("am")      #counts the occurrence of substr in string
print(a)
print(b)
print(c)
print(d)
print(e)

name=input("Enter name: ")
print(len(name))
print(name.count("a"))


# replace :- to replace the data
str = "Hello i am learning Python, Python is very easy language, Python is beginner friendly"
print(str.replace("Python", "C"))

# find :- to find a string in substring
print(str.find("learning"))