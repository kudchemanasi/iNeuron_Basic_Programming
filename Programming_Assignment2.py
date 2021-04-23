#1.	Write a Python program to convert kilometers to miles?
km=float(input("Enter KM value:"))
miles=km*0.6213
print(miles)

#2.	Write a Python program to convert Celsius to Fahrenheit?
Cel=float(input("Enter Celsius value:"))
Far=(9/5)*Cel+32
print(Far)

#3.	Write a Python program to display calendar?
import calendar
yy=int(input("Enter year:"))
mm=int(input("Enter month"))
print(calendar.month(yy,mm))

#4.	Write a Python program to solve quadratic equation?
import cmath
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
d=(b*b)-(4*a*c)
x1=-b+cmath.sqrt(d)/2*a
x2=-b-cmath.sqrt(d)/2*a
print("{}{}".format(x1,x2))

#5.	Write a Python program to swap two variables without temp variable?
a=input("Enter the value of a")
b=input("Enter the value of b")
a,b=b,a
print('a=', a)
print('b=',b)










