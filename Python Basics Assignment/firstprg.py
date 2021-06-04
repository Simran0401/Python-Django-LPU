"""
Q1. From this given string: s = "Hey i am from New Delhi". 
Find out: length of string, convert this to list using split operation. 
"""


def Convert(string):
    li = list(string.split(" "))
    return li
     
s = "Hey i am from New Delhi"
print(len(s))
print(Convert(s))
