#Write a Python program to calculate the area of regular polygon.
import math
n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
S= (n * a * a) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(S))