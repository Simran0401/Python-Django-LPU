'''
Q2. Print all odd numbers and even numbers between 1 to 100
'''

start = 1
end = 100

print("All odd numbers from 1 to 100 are:")
for i in range(start, end + 1):
    if(i % 2 != 0):
        print(i, end = " ")

print("\n")

print("All even numbers from 1 to 100 are:")
for i in range(start, end + 1):
    if(i % 2 == 0):
        print(i, end = " ")
