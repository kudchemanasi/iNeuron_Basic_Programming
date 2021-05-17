#1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fabo(n):
    if n<=1:
        return n
    else:
        return (fabo(n-1)+fabo(n-2))
Seq=int(input(":"))
if(Seq<=0):
    print("Positive integer")
else:
    print("Fibonacci Series")
    for i in range(Seq):
        print(fabo(i))

#2.	Write a Python Program to Find Factorial of Number Using Recursion?
def fact(n):
    if(n==1):
        return n
    else:
       return n*fact(n-1)
num=int(input(":"))
if(num==0):
    print("Factorial is 1")
elif(num<=1):
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        print(fact(i))
#4.	Write a Python Program to calculate the natural logarithm of any number?
import math
print(math.log(100))

#5.	Write a Python Program for cube sum of first n natural numbers?
num=int(input())
sum=0
if(num<1):
    print("NO sum")
else:
    for i in range(1,num+1):
        sum=i**3
        print("Sum is:",sum)

