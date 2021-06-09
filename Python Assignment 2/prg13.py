'''
Q13. Write a program that accepts a sentence (string) and calculate the number of letters and digits.
Example: ‘this is a test sentence number 389’ ==> letters = 25 and digits = 3.
'''

str = input("Enter the required string: ")
digits = 0
letters = 0
for s in str:
    if s.isdigit():
        digits = digits + 1

    elif s.isalpha():
        letters = letters + 1

    else:
        pass

print("Letters = ", letters, "and", "digits = ", digits)
