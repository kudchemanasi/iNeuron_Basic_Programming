"""Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
"""
class Generator:
    def __init__(self,num):
        self.num=num
        print("Print the iterator")
    def iterator(self,num):
        for i in range(0,self.num):
            if (i%5==0 and i%7==0):
                print(i)
num=Generator(100)
num.iterator(100)

"""Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
"""
def EvenGen(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(input())
values = []
for i in EvenGen(n):
    values.append(str(i))
print(",".join(values))

"""Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
"""
def fibo(n):
    if (n<1):
        print("1")
    elif (n==1):
        print(n)
    else:
        print(fibo(n-1)+fibo(n-2))
n=int(input("Enter num"))
print(fibo(n))

"""Question 4:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john"""

import re
Email=input("Emailid:")
x="(\w+)@(\w+)\.(com)"
r=re.match(x,group(2))
print(r.group(2))

"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default"""
class shape:
    def __init__(self,length):
        self.length=length
class square(shape):
    def area(self):
        print("Area is 0 by default")
obj=square(7)
obj.area()
