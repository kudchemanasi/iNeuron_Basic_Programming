#1.	Write a Python Program to Find the Factorial of a Number?
a=int(input("Enter the value of a:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
    print(fact)

#2.	Write a Python Program to Display the multiplication Table?
Table=int(input("Enter num:"))
for i in range(1,11):
    num=Table*i
    print(num)
#3.	Write a Python Program to Print the Fibonacci sequence?
num=int(input("Enter num:"))
first=0
second=1
while(i<num):
    if(i<=1):
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)
    i=i+1
#4.	Write a Python Program to Check Armstrong Number?
num=int(input("Enter a num:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an Armstrong")
else:
    print("No armstrong",num)

#6.	Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("Enter the num:"))
sum=0
for i in range(1,n):
    sum=sum+i
    print(sum)
