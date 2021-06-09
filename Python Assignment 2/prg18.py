'''
Q18. Write a program which accepts two strings s1 and s2 and checks if s2 is a substring of s1.
'''

def isSubstring(s1, s2):
    a = len(s1)
    b = len(s2)
 
    for i in range(a - b + 1):
        for j in range(b):
            if (s1[i + j] != s2[j]):
                break
             
        if j + 1 == b :
            return i
 
    return -1
 

if __name__ == "__main__":
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")

    result = isSubstring(s1, s2)

    if result == -1 :
        print("s2 is not a substring of s1")
    else:
        print("s2 is a substring of s1 from index " + str(result))
 