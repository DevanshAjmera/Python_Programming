# Square root of a number
a = 25
print(f"Square root of {a} is { a**(0.5) }")

# By newton method
"""
x = root (a)
x^2 = a

f(a) = x^2 - a

x = x - f(a)/ f'(a)
x = x - (x^2 - a)/(2x) 
x = x - (x/2 - a/2x)
x = x - x/2 + a/2x
x = x/2 + a/2x
x = 0.5 * (x + a/x)


"""
x = a
for i in range (10):
    x = 0.5 * (x + a/x)

print(x)