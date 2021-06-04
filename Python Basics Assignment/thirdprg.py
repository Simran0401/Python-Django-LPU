"""
Q3. Using length and breadth as input find out area and perimeter of a given rectangle.
"""

length = int(input("Length: "))
breadth = int(input("Breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the given Rectangle: ", area)

print("Perimeter of the given Rectangle: ", perimeter)