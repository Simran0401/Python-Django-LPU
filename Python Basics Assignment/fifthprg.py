"""
Q5. Write a program to compute roots of a quadratic equation when
coefficients a, b and c are known(entered by user).
"""

import cmath

a = float(input("Value of Cofficient a: "))
b = float(input("Value of Cofficient b: "))
c = float(input("Value of Cofficient c: "))

d = (b ** 2) - (4 * a * c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print('The roots are {0} and {1}'.format(root1, root2))