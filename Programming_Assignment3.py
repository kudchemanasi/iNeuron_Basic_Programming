#1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
num=int(input("Enter the number:"))
if(num==0):
    print("O")
elif(num>=0):
    print("Positive")
else:
    print("Negative")

#2.Write a Python Program to Check Leap Year?
year=int(input("Enter Year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#3.	Write a Python Program to Check if a Number is Odd or Even?
num=int(input("Enter a number:"))
if(num%2==0):
    print("Number is Even")
else:
    print("Number is odd")

#4.	Write a Python Program to Check Prime Number?
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num,"is a prime number")

#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower=int(input("Enter lower num:"))
upper=int(input("Enter upper num:"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


