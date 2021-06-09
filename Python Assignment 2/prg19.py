'''
Q19. Make a password validator with the following checks. A website requires the users to
input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
1. At least 1 letter between [a-z]     
2. At least 1 number between [0-9]     
3. At least 1 letter between [@$#%&]
'''

import re
password = input("Enter a password: ")
flag = 0

while True:  
    if not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[@$#%&]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag == -1:
    print("Not a Valid Password")
