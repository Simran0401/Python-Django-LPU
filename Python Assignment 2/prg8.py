'''
Q8. Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

n = range(1, 101)
a = sum(n)
print (abs(sum(i * i for i in n) - a * a))