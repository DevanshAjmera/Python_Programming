#File :- collection of related data stored at memory
    #Text file :- data stored in character form (.txt, .docx, .log)
    #Binary file :- (.mp4, .mov, .png, .jpeg)
#operation in file
"""
Modes: - 
    1. r :- reading a file
    2. w :- write content into file after truncating( removing all previous data) it
    3. a :- write content at the end without truncating it
    4. r+ :- read and write (stream(pointer) is at beginning, overwrite data from beginning)
    5. w+ :- write and read (truncating file)
    6. a+ :- append and read (stream at last, no truncating)
    7. t :- used for text files (rt, wt)
    8. b :- used for binary files (rb, wb)

create and write data into file:-
    f=open("filename.extension","w")
    f.write("your msg")
    f.close()

read data from file :-
    f=open("filename.extension","r")
    print(f.read())

delete file :-
    import os
    os.remove("filename.extension")
"""


"""
f = open("Filehandling.txt","a+")
print(f.read())   # blank line as stream points to last of file
f.write("python3")    # append (add at the last of file)
print(f.read())  # stream points to last hence no char left (only blank line)
f.close()

with open("Filehandling.txt","r") as f:  # automatically closes the file without (f.close)
    print(f.read(2100))
    print(f.read())   # gives  a blank line
"""


# Create a file
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")    # to replace a sub-string with another in a file
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)



"""
def check_for_word(word):                   # To check if a word is found in file or not
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):  # or if(word in data)
            print("Found at index",data.find(word))
        else:
            print("Not found")
check_for_word("learning")


def check_for_line(word):    # To check a word in a file and give the line number as output
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Word found at line number",line_no)
                return 1
            line_no += 1
        return -1
print(check_for_line("Python"))
"""


"""
with open("numbers.txt","r") as f:    # Scratch code for counting of even numbers in a file.
        data = f.read() 
        num = ""
        for i in range(len(data)):
            if (data[i] == ","):
                print(int(num))
                num = ""
            else:
                num += data[i]

def count_even():            # Function to count even numbers in a file (containing numbers separated by commas)
    count = 0
    with open("numbers.txt","r") as f:
        data = f.read()
    list = data.split(",")
    for i in list:
        if (int(i) % 2 == 0):
            count += 1
    print(count)
count_even()
"""