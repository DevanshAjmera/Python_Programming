# Set is collection of unordered, no duplicate(ignores in output)
# Set is mutable(add, remove, clear, pop) but elements are immutable(unchangeble). 
# It is used to store multiple data types.

#To create an empty set, you can use set() function.
Set1 = set()
print(type(Set1))  # <class 'set'>

mySet={"Devansh","Viyom","Prince","Viyom"}
print(mySet)
#mySet[0] = "Piyush"  # not add becoz. set does not modify data...

print(" ")


names_set = {'Pawan', 'Devansh', 'Viyom', 'Prince'}
print(names_set)
names_set.remove("Pawan")
print(names_set)
names_set.remove('Devansh')
print(names_set)
names_set.add("Devansh Ajmera")
print(names_set)
names_set.add('Devansh')
print(names_set)
names_set.pop()         # Remove a random element
print(names_set)
print(len(names_set))   # Length of the set
names_set.clear()       # Clear the set
print(len(names_set))   # Length of the set after clearing



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))  # Union of two sets (combines all elements)
print(set1.intersection(set2))  # Intersection of two sets (common elements)