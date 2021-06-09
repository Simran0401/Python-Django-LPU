'''
Q4. Write a program that asks the user for a number n and prints the sum of the numbers
1 to n such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17.
'''

x = 1
sum = 0

n = int(input("Enter a number: "))

for i in range(x, n + 1):
    if (i % 3 == 0) or (i % 5 == 0):
        sum = sum + i

print(sum)    
