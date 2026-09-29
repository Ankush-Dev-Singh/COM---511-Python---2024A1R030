# 1. Store two points as tuples and calculate distance
import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
p1 = (x1, y1)
p2 = (x2, y2)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Point 1:", p1)
print("Point 2:", p2)
print("Distance:", distance)