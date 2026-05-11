a=input("Enter sentence: ")
b=a.split()
for ch in b:
    print(ch,"=",b.count(ch))