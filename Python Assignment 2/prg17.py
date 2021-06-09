'''
Q17. Write a program to find if a given string is a palindrome or not.
'''

def isPalindrome(str):
 
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
s = input("Enter the required string: ")
result = isPalindrome(s)
 
if (result):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")