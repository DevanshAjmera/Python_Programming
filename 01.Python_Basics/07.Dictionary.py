# Dictionary can store the data in key-value pair
# can be update, pop, del
# unordered, no duplicate keys, mutable(changeable)

myInfo = {"name":"Devansh Ajmera","email":"d@gmail.com","mobile":"12345678","age":18,"name":"Devansh"}
print(myInfo)
print(type(myInfo))
print(myInfo["mobile"])
print("My name is" ,myInfo["name"],"mobile number is",myInfo["mobile"],"and age is", myInfo["age"], "and email is",myInfo["email"])
print(f"My name is {myInfo["name"]} mobile number is {myInfo["mobile"]} and age is {myInfo["age"]} and email is {myInfo["email"]}")

#to access the complete dictonary key...
for value in myInfo.keys():
    print(value)

#to access the complete dictonary value...
for value in myInfo.values():
    print(value)

# to get dictionary as tuple
print(myInfo.items())

# to get the key by get method 
print(myInfo["name"])           # This will give error if key not found
print(myInfo.get("name"))       #Returns None if not found
print(myInfo.get("mobile"))

# to upadate the values in dictonary...
myInfo["name"]="DEVANSH AJMERA"
myInfo["age"]=18
myInfo["email"]="d@outlook.com"
myInfo["mobile"]="12345678"
for i in myInfo.values():
    print(i)
print(" ")


myInfo.update({"gender":"male"})    #update the values

for i in myInfo.values():
    print(i)


myInfo.pop("email")
print(" ")
for i in myInfo.keys():
    print(i)

del myInfo["mobile"]
print(myInfo)