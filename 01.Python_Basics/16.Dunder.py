"""Dunder or magic methods in Python.
Dunder methods are special methods that start and end with double underscores.

Types of dunder methods:
1. Binary Opeartors: __add__, __sub__, __mul__, __truediv__, etc.
2.Extended assignment operators: __iadd__, __isub__, __imul__, __itruediv__, etc.
3. Unary Operators: __neg__, __pos__, __abs__, etc.
4. Comparison Operators: __eq__, __ne__, __lt__, __le__, __gt__, __ge__.
"""

class Equality:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return (self.value == other.value)
    
eq1 = Equality(178)
eq2 = Equality(17)
print(eq2 == eq1)  # True, because __eq__ is defined


class message:
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):     #representation method : used for debugging and logging
        """Return a string representation of the object."""
        return 'object:{}'.format(self.msg)
    def __add__(self, other):
        """Define the behavior of the + operator."""
        return self.msg + other
    
if __name__ == '__main__':
    obj = message('Hello')
    print(obj + "World")  # object:Hello
   
 