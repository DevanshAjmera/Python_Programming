"""class, objects (creation, deletion),
inheritance(single, multiple, multilevel, hierarchical, hybrid(multiple, multilevel)), 
polymorphism (method overriding, method overloading, operator overload),
Abstraction, Encapsulation, 
DECORATORS (@staticmethod (without self), @classmethod, @property)
"""


# Class -> is blueprint for creating objects (collection of attributes and methods)
# rules: 1st letter is in uppercase for class
class Devansh:
    '''DOCUMENTAION'''   #can be accessed by obj.__doc__
    print("My name is Devansh Ajmera.")
    age=18
    email = "devanshajmera10@gmail.com"

#object (instances of class) creation
devansh : Devansh = Devansh()     # or obj_name = class_name()
devansh.__doc__
print("My age is",devansh.age,"\n")



"""
class Student:
    name = "Devansh"
    email = "d@gmail.com"
    def findMyAge(this, cY, bY):      #this -> passes current class reference...
        ageInYear = cY-bY
        print(ageInYear)
    def Monthly_Pocket_Money(this,weekly_money):
        totalMoney = weekly_money*4
        print("My Pocket Money",totalMoney)
        #print("Monhly pocket money is",weekly_money*4)
stu = Student()
stu.findMyAge(2025,2005)
#stu.Monthly_Pocket_Money(200)
stu.Monthly_Pocket_Money(int(input("Enter Weekly money: ")))
"""


"""
#Calculate the top speed of the car if each gear increase car speed by 50 km/h.
class Car:
    model= 2024
    gears= 7 
    first_gear=50
    
    def top_speed(this, gear):
        print("The top speed is :",50*gear)
car: Car = Car()
car.top_speed(int(input("Enter gear number (1-5) : ")))
"""


"""
# Constructor :- automatically calls when obj is created def __init__(self, par1, par2, ...)
class Details:
    name = "anonymous"   # Preference (obj attr > class attribute)
    college_name = "ITS"   # class attribute..(can be accessed by obj.attribute or class_name.attribute)
    def __init__(self, name, age):
        self.name = name   # object attribute (eg. self.name)
        self.age = age
student1 = Details("Devansh", 19)
student2 = Details("Aryan",20)
student3 = Details("Viyom",20)

print(student1.name, student1.age, student1.college_name)
print(student2.name, student2.age, student2.college_name)
print(student3.name, student3.age, student3.college_name)
"""



"""
# Create a Student class that takes name & marks of 3 subjects as arg in constructor. Then create a method to print the average
class Student:
    def __init__(self ,name , marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        return (sum)/3
print("\n")
s1 = Student("A", [100, 95, 97])
s2 = Student("B", [89, 91, 97])
s3 = Student("C", [90, 98, 96])
print(s1.name,"got",s1.average())
print(s2.name,"got",s2.average())
print(s3.name,"got",s3.average())
"""

# STATIC METHODS :- methods that don't use self parameter (work at class level)
class Student:
    @staticmethod  # decorator: allow to wrap function to change its behaviour, without permanently modifying it. 
    def college():
        print("ABC College")
s1 = Student()
s1.college()

"""
# ABSTRACTION :- Hiding internal or implementational details and showing functinality, features to users.
# ENCAPSULATION :- Wrapping of code and data in a single unit.
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amt):
        self.balance -= amt
        print("Rs", amt, "was debited")
    
    def credit(self, amt):
        self.balance += amt
        print("Rs", amt, "was credited")
    
    def get_balance(self):
        return self.balance

customer1 = Account(10000,100001)
customer1.debit(2000)
customer1.credit(5000)
print(customer1.get_balance())
# del :- to delete object properties or object itself (del obj_name)
del customer1



# Private attributes & methods are meant to be used only within class and are not accessible from outside the class
# to make an attribute private (self.__attribute = attribute)
class Account:
    __name = "anonymous"   # private data member
    def __hello():         # private method
        print("Hello person!")   
    def __init__(self, account_no, account_pass):
        self.account_no = account_no         # public attribute
        self.__account_pass = account_pass   # private attribute
    def reset_pass(self):
        print(self.__account_pass)   # private attribute accessible in class

a1 = Account(101, 1234)
print(a1.account_no)
# print(a1.__name) not accessible..
# print(a1.__hello())  not accessible
# print(a1.__account_pass)   not accessible becoz. of private   
a1.reset_pass()   
"""



# Inheritance :- process of acquiring properties and behaviours of parent or base class to child class.
# 1. Single Inheritance :- one base class and one derived class.
# 2. Multiple Inheritance :- multiple base classes and one derived class.
# 3. Multilevel Inheritance :- one base class and one derived class and so on.
# 4. Hierarchical Inheritance :- one base class and multiple derived classes.
# 5. Hybrid Inheritance :- combination of multiple inheritance and multilevel inheritance.
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):   # single inheritance
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

class Fortuner(Car):   # multilevel inheritance
    def __init__(self, type):
        self.type = type

class Color(ToyotaCar, Fortuner):   # multiple inheritance
    def __init__(self, color):
        self.color = color

car1 = Fortuner("Petrol")
car2 = Color("Black")
car2.start
car1.start()  # car started
car3 = ToyotaCar("Prius", "Electric")
print(car3.type)  # electric


# Class method :- method that is bound to class and not the object of the class. 
# It takes cls as the first parameter which points to the class and not the object instance.
class Person:
    name = "anonymous"
    def change_name(self, name):
        self.__class__.name = name  # class attribute
        #Person.name = name # class attribute
    @classmethod
    def change_name(cls, name):
        cls.name = name  # class attribute
p1 = Person()
p1.change_name("Devansh")
print(p1.name)  # Devansh
print(Person.name)  # Devansh

# Property method :- decorator that allows you to define a method as a property of a class.
# It allows you to access a method as an attribute without calling it like a method.
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
        
stu1 = Student(90, 80, 70)
print(stu1.percentage)  # 80.0%
stu1.phy = 100
print(stu1.percentage)



# Polymorphism :- ability to take many forms. It allows you to define a single interface for a group of related classes.
# It allows you to use a single function or method in different ways.
# 1. Operator Overloading :- changing the meaning of an operator for user-defined classes.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def show_number(self):
        print(f"{self.real} + {self.imag} i")
    
    def __add__(self, num2):   # Dunder (Double underscore) method for operator overloading
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return Complex(newreal, newimag)
    
    def __sub__(self, num2):   # Dunder (Double underscore) method for operator overloading
        newreal = self.real - num2.real
        newimag = self.imag - num2.imag
        return Complex(newreal, newimag)
c1 = Complex(2, 3)
c1.show_number()  # 2 + 3i
c2 = Complex(4, 5)
c2.show_number()  # 4 + 5i
c3 = c1 + c2  # c3 = c1.__add__(c2)   # operator overloading
c3.show_number()  # 6 + 8i
c3 = c1 - c2  # c3 = c1.__sub__(c2)   # operator overloading
c3.show_number()  # -2 - 2i

# 2. Method Overriding :- redefining a method in the derived class that is already defined in the base class.
# 3. Method Overloading :- same method name with different number of parameters or different types of parameters.  ""

"""
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
c1 = Circle(10)
print("Area of circle is",c1.area())
print("Perimeter of circle is",c1.perimeter())
"""

"""
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showdetails(self):
        print("Role is",self.role, end = ", ")
        print("Department is",self.dept, end = ", ")
        print("Salary is",self.salary)

class Engineer(Employee):
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        super().__init__("Engineer", dept, 60000)
    def showdetails(self):
        print("Name is",self.name, end = ", ")
        print("Age is",self.age, end = ", ")
        print("Role is",self.role, end = ", ")
        print("Department is",self.dept, end = ", ")
        print("Salary is",self.salary)

e1 = Engineer("Devansh", 19, "IT")
e1.showdetails()  # Name is Devansh, Age is 19, Role is Engineer, Department is IT, Salary is 60000
"""

"""
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, order2):
        return self.price > order2.price
o1 = Order("Tea", 100)
o2 = Order("Coffee", 200)
print(o1 > o2)  # Order 1 is greater than Order 2
print(o2 > o1)  # Order 2 is greater than Order 1
"""