'''
Q20. s = "Hello how are you all". For this given string write a code such that it prints
the vowels present in the string s if any. ex: "i", "a" etc.
'''

s = "Hello how are you all"
vowels = "AaEeIiOoUu"

result = set([each for each in s if each in vowels])
print("The vowels present in the string: ", result)
