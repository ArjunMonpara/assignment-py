#Write a Python function to get the largest number, smallest num and sum of all from a list.
def find(num):
    a=max(num)
    b=min(num)
    c=sum(num)
    print("max is",a)
    print("min is",b)
    print("sum is",c)
num=[20,45,12,69]
find(num)