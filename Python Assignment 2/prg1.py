'''
Q1. Write a program to print all the natural numbers from 1 to n (user input).
Then print the same in reverse order.
''' 


n = int(input("Enter any number: "))

print("Natural numbers from 1", "to", n) 

for i in range(1, n + 1):
    print (i, end = '  ')

print("\n");

print("Natural numbers in reverse from", n, "to", "1")     

while ( n >= 1):
    print (n, end = '  ')
    n = n - 1    