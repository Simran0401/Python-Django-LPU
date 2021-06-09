'''
Q14.  Write a program that accepts a string and outputs the string with all capital letters.
Example: ‘hello’ ==> ‘HELLO’. (using loop)
'''

def upperCase(str):
    lenOfStr = len(str)
 
    for i in range(lenOfStr):
        if str[i] >= 'a' and str[i] <= 'z':
            str[i] = chr(ord(str[i]) - 32)
 
if __name__ == "__main__":
    str = input("Enter the required string: ")
    str = list(str)

    upperCase(str)
 
    str = ''.join(str)
    print("The string in uppercase is: ", str)
