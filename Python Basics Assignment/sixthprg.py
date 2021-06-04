"""
Q6. Find volume of a sphere using radius as input.
"""

radius = float(input("Enter the radius of the sphere: "))
pi = float(22/7);

volume = 4 * ((pi * (radius * radius * radius))) / 3

print("Volume of the sphere: ", volume)