#Write a Python function to insert a string in the middle of a string. 
def insert(a,b):
    mid=len(a)//2
    c=a[:mid]+b+a[mid:]
    print(c)
insert("Hello", "Arjun")