#Write python program that swap two number with temp variable and without temp variable. 

#with temp variable
a=10
b=23
print("Befor swap: ")
print("a is ",a)
print("b is ",b)
temp=a
a=b
b=temp
print("After swap: ",a,b)


#without temp variable
a=20
b=68
print("Befor swap: ",a,b)
a,b=b,a
print("After swap",a,b)