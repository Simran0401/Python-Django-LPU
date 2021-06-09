'''
Q16. Write  a program that counts the occurrence of a character in a string.
Example: ‘This is a test string.’ count of i = 3.
'''

def count(str, c) :
      
    occurence = 0
      
    for i in range(len(str)) :
        if (str[i] == c):
            occurence = occurence + 1
    return occurence
      
s = input("Enter the required string: ")
c = input("Enter the required character: ")

print("Count of", c, "=", count(s, c))