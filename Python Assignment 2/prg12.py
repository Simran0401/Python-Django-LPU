'''
Q12. Find the length of a string using loops (not len()).
'''

#This is using for loop

def findLength(str):
    count = 0    
    for i in str:
        count += 1
    return count
  
str = input("Enter the required string: ")
print(findLength(str))

'''
This is using while loop

def findLength(str):
    count = 0
    while str[counter:]:
        count += 1
    return count
  
str = input("Enter the required string: ")
print(findLength(str))

'''