'''
Q5. Write a program that asks the user for a number n and gives them the possibility
to choose between computing the sum and computing the product of 1,…,n.
'''

num = int(input("Enter a number: "))

choice = int(input("Enter 0 for sum and 1 for product: "))

sum = 0
product = 1

for i in range(1, num + 1):
    if choice == 0:
        sum = sum + i
        
    elif choice == 1:
        product = product * i
        
    else:
        print("Required output will be shown only if 0 or 1 is entered")

if choice == 0:
    print(sum)

if choice == 1:
    print(product)
