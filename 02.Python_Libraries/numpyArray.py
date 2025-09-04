# 1. Numpy: it is used to work on large data set
# 2. Range is too large
# 3. High order function
# 4. Array Reshape
# 5. Create N dimension array

# How to use numpy in python:- goto terminal -> pip install numpy
import numpy as np

#assign array in numpy
myData = np.array([1,2,3,4]) 
print(myData)       #[1 2 3 4]
print(type(myData)) #<class 'numpy.ndarray'>

myData[0]=9
myData[1]=10
myData[2]=11
myData[3]=12
print(myData)

y=9
for i in range(0,4):
    myData[i]=y   # or , myData[i]= i + y
    y=y+1
print(myData)

i=0
x=12
while i < 4:
    myData[i] = x - i
    i=i+1
print(myData)


# Access the data from numpy array
for data in range(0,4):
    print(myData[data])

myFriends = np.array(["ivan","anshu","wani","anjani"])
for name in myFriends:
    print(name)

# print the reverse of a array
i=3
while i >= 0:
    print(myFriends[i])
    i = i-1

myFriends.sort()
print(myFriends)