#Write a Python function that takes a list of words and returns the length of the longest one. 
def longest(words):
    maxlen=0
    for ch in words:
        if len(ch) > maxlen:
            maxlen = len(ch)
    return maxlen
list=["arjun","aditya","parv"]
print("Longest length =",longest(list))