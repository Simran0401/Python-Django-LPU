"""
Q2.  Given string s = "name is rahul". Write code to give following o/p.
- "Name is rahul"
- "Rame Is Rahul"
- "NAME IS RAHUL"
"""

s = "name is rahul"
print(s.capitalize())

str = s.replace("name", "rame")
print(str.title())

print(s.upper())