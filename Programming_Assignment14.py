"""Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""
class generator():
    def __init__(self,num):
        self.num=num
    def iterate(self):
        for i in range(0,self.num):
            if(i%7==0):
                print("Divisible")
            else:
                print("Not Divisible")
x=generator(int(input()))
x.iterate()

"""Question 3:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""

class Male():
    def getGender(self):
        print("Male")
class Female():
    def getGender(self):
        print("Female")
class Person(Male,Female):
    def getGender(self):
        print("Print the gender")
gender=Person()
gender.getGender()

"""Question 4:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

res = [[i, j, k] for i in subjects
                 for j in verbs
                 for k in objects]
for x in res:
    print(" ".join(x))

"""Question 5:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))

6""".Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list."""
def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2


        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")




