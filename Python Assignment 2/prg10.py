'''
Q10. Pattern:

- >

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5

->
5 5 5 5 5 
5 4 4 4 5 
5 4 3 4 5 
5 4 4 4 5 
5 5 5 5 5

->
* 
* * 
* * * 
* * * * 
* * * * * 

->
****
***
**
*

->
#####
#####
#####
#####
#####
'''

print("->")

for num in range(6):

    for i in range(num):

        print(num, end = " ")

    print("\n")

print("->")


N = 5
len = N
minimum_val = 0
for i in range(0,len):
    for j in range(0,len):
        if i  < j :
            minimum_val = i
        else:
            minimum_val = j

        if minimum_val < len-i:
            minimum_val = minimum_val
        else:
            minimum_val = len-i-1
        
        if minimum_val < len-j-1:
            minimum_val = minimum_val
        else:
            minimum_val = len-j-1

        print(N-minimum_val,end = " ")

    print("\n") 


print("->")

def pattern(n):
    
    for i in range(0, n):
        for j in range(0, i+1):
         
            print("* ",end="")
      
        print(" ")
        
 
n = 5
pattern(n)

print(" ")
print("->")

rows = 4
 
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end = "")  
    print("")

print("->")

numOfRows = 5
numOfColumns = 5

i = 0
while(i < numOfRows):
    j = 0
    while(j < numOfColumns):
        print('#', end = "")
        j = j + 1
    i = i + 1
    print("")

