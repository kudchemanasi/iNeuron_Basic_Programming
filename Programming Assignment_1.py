#1.	Write a Python program to print "Hello Python"?
print("Hello Python")

#2.	Write a Python program to do arithmetical operations addition and division?
a = int(input("Enter the value of a"))
b= int(input("Enter the value of b"))
z =(a+b)
y =(a/b)
print(z)
print(y)

#3Write a Python program to find the area of a triangle?
b= float(input("Enter the value of base"))
h= float(input("Enter the value of height"))
a=(1/2)*b*h
print(a)

#4.	Write a Python program to swap two variables?
a=input("Enter the value of a")
b=input("Enter the value of b")
a,b=b,a
print('a=', a)
print('b=',b)

#5.	Write a Python program to generate a random number?
import random
print(random.randint(0,50))