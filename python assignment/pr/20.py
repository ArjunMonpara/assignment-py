#Write a Python program to remove duplicates from a list. 
a=[10,20,30,85,20,10,30,1,2,20,5,5,14,14,39,494,85]
b=[]
print("original list is:")
print(a)
for i in a:
    if i not in b:
        b.append(i)
print(b)