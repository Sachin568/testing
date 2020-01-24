"""
@author: sachin paramesha

"""
from numbers import Number

def classify_triangle(a, b, c):
    """
    This function returns the string depending on the lenghts of the triangles

    """
    if not isinstance(a, Number) or not isinstance(b, Number) or not isinstance(c, Number):
        return 'Not a triangle'

    sides = [a, b, c]       # adding lengths to list and sorting the list of lengths
    sides.sort()

    if sides[0] == sides[1] == sides[2]:
        return "Equilateral triangle"

    if (sides[0] <= 0 or sides[2] <= 0) or (sides[0] + sides[1] <= sides[2]):
        return "Not a triangle"

    if sides[0] == sides[1] and sides[0] != sides[2]:
        return "Isosceles triangle"

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "Right angle triangle"
    
    else:
        return "Scalene triangle"

# driver code
print(classify_triangle(6, 7, 6))
