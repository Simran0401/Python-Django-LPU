"""
Q4. Using diameter as input find out circumference and area of a circle.
"""

pi = float(22/7)
diameter = int(input("Diameter: "))

circumference = pi * diameter
area = (pi * (diameter * diameter))/4

print("Circumference of the circle: ", circumference)

print("Area of the circle: ", area)