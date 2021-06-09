'''
Q15. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''

def Calculate(str):
    upper = 0
    lower = 0

    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1

    print('Upper case letters: ', upper)
    print('Lower case letters: ', lower)

str = input("Enter the required string: ")

Calculate(str)