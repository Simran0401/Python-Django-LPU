"""
Q9. Write a program to that accepts a string s, an index number n and a character ‘c’.
 And outputs the string replaced with the character at the index number n. 
 Example- ‘hello’ , 0 , ‘j’ ==> ‘jello’.
(Hint2: You can try it by join function too by typecasting it to list)
"""
  
 
s = input("Enter the string: ")
n = int(input("Enter the index: "))
c = input("Enter the character: ")
        
str = s[0:n] + c + s[n + 1:]

print(str);
 