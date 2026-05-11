#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
num1=int(input("enter num1: "))
num2=int(input("enter num1: "))
num3=int(input("enter num1: "))
sum=num1+num2+num3
if num1==num2 or num1==num3 or num2==num3:
    print("Sum is zero")
else:
    print("Sum is: ",sum)

