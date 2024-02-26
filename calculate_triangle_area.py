"""
Calculate the area of a triangle
"""

# float has been used instead of integer to give more room for numbers
side1 = float(input("Please enter the first side of the triangle: "))
side2 = float(input("Please enter the second side of the triangle: "))
side3 = float(input("Please enter the third side of the triangle: "))
s = ((side1 + side2 + side3) / 2)

# Import math library
import math

#Alternatively, use ** 0.5 instead of square root function
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is: ", area)