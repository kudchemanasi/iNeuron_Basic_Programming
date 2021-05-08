#1.	Write a Python Program to Find LCM?
def LCM(num1,num2):
    if (num1>num2):
        greater=num1
    else:
        greater=num2
    for i in range(1, greater + 1):
        if((greater%num1==0) and (greater%num2==0)):
            lcm=greater
            break;
        greater+=1
    return LCM

x=int(input("Enter num1:"))
y=int(input("Enter num2:"))
print("LCM of",x,"and",y,"is",LCM(x,y))

#2.	Write a Python Program to Find HCF?
def hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("The H.C.F. is",hcf(num1, num2))

#3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
def decimalToBinary(n):
    return bin(n).replace("0b", "")
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))

#4.	Write a Python Program To Find ASCII value of a character?
char=input("Enter char:")
print("The ascii value of char is",ord(char))

#Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1%num2
a=float(input("Enter a:"))
b=float(input("Enter b:"))
print("Addition\n",addition(a,b),"subtraction:\n",subtraction(a,b),"multiplication:\n",multiplication(a,b),"division:\n",division(a,b))

