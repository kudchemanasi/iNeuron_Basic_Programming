#1.	Write a Python Program to Add Two Matrices?
import numpy as np
sum=0
f=np.array([[1, 2, 3], [4, 5, 6],[7,9,8]])
g=np.array([[1, 2, 3], [4, 5, 6],[7,9,8]])
sum=f+g
print(sum)

#2.	Write a Python Program to Multiply Two Matrices?
import numpy as np
mul=1
f=np.array([[1, 2, 3], [4, 5, 6],[7,9,8]])
g=np.array([[1, 2, 3], [4, 5, 6],[7,9,8]])
mul=f*g
print(mul)

#4.	Write a Python Program to Sort Words in Alphabetic Order?
my_str = input("Enter a string: ")
words = my_str.split()
words.sort()
for word in words:
   print(word)

#5.	Write a Python Program to Remove Punctuation From a String?
def Punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    print(string)
string = input("String")
Punctuation(string)





