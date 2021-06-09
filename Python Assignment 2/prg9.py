'''
Q9. Write a program which can compute the factorial of a given number.
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
n = int(input("Enter a number: "))

print(factorial(n))