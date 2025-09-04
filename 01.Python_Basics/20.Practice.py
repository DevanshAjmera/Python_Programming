"""
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if(n1 > n2 and n1 > n3 and n1 > n4):
    print(n1,"is greater.")
elif(n2 > n1 and n2 > n3 and n2 > n4):
    print(n2,"is greater.")
elif(n3 > n1 and n3 > n2 and n3 > n4):
    print(n3,"is greater.")
elif(n4 > n1 and n4 > n2 and n4 > n3):
    print(n4,"is greater.")

"""


"""
list =[]
a=input("Enter movie1 name: ")
b=input("Enter movie2 name: ")
c=input("Enter movie3 name: ")

list.append(a)
list.append(b)
list.append(c)

print(list)
"""


"""
# Palindrome check using list
# A palindrome is a word, that reads the same forward and backward 
# (ignoring spaces, punctuation, and capitalization).
list1 = [1,2,3,2,1,]
list2 = list1.copy()
list2.reverse()
if (list1 == list2):
    print("Palindrome")
else:
    print("Not Palindrome")
"""


"""
grade = ("C","D","A","A","B","B","A")
print("The students with Grade A are:", grade.count("A"))
Grade_list = []
for i in range(len(grade)):
    Grade_list.append(grade[i])

Grade_list.sort()  # Sort in ascending order
# Grade_list.sort(reverse=True)  # Sort in descending order
print(Grade_list)
"""


"""
dict1 = {
    "table" : {"a piece of furniture","list of facts & figures"},
    "cat" : "a small animal"
}
print(dict1)
set1 = {"python", "java", "C++", "python", "javascript","java","python","java","C++","C"}
print(f"The total number of classromms needed : {len(set1)}")
"""


"""
dict2= {}
s1 = input("Enter subject name 1: ")
sa = int(input("Enter marks 1: "))
s2 = input("Enter subject name 2: ")
sb = int(input("Enter marks 2: "))
s3 = input("Enter subject name 3: ")
sc = int(input("Enter marks 3: "))
dict2.update({s1:sa, s2:sb, s3:sc})
print(dict2)
"""


"""
n = 100
i = 1
while i <= 10:
    print(i*i,)
    i=i+1

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


k = 0
while k < len(tup):
    print(tup[k])
    k+=1
"""


"""
list = [1,2,3,4,5,6,7,8,9,10]
def length(list):
    return len(list)
print("Length of the list is: ", length(list))

def elements (list):
    for item in list:
        print(item, end =" ")
elements(list)
"""


"""
num = int(input("Enter a number: "))
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact*=i
        i+=1
    return fact
print(factorial(num))


# Currency Convertor 
def currency_convertor(rs, usd = 84.5):  #default parameter
    print("Indian rupee =",rs*usd)
currency_convertor(5)


num = int(input("Enter num: "))
def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_even(num))
"""