#Write a Python program to get the Fibonacci series of given range.
n=int(input("Enter: "))
a=0
b=1
print("Fibonacci Series: ")
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c