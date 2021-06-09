'''
Q3. Write a program to check if a number is prime or not. Example: 7 ==> True, 6 ==> False
'''

n = int(input("Enter a number: "))
flag = False

if(n > 1):
    for i in range(2, n):
        if (n % i) == 0:
           print(n,"is not a prime number")
           break
    else:
       print(n,"is a prime number")
 
else:
   print(n,"is not a prime number")