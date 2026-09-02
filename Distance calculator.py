import math

# Ask the user to enter the coordinates of the first point
point_x1 = float(input("Enter x1: "))
point_y1 = float(input("Enter y1: "))

# Ask the user to enter the coordinates of the second point
point_x2 = float(input("Enter x2: "))
point_y2 = float(input("Enter y2: "))

#distance = sqrt(pow(point_x2-point_x1, 2) + pow(point_y2-point_y1, 2))

# Compute the distance using the easier way
point_a = pow(point_x2-point_x1, 2)
point_b = pow(point_y2-point_y1, 2)
result = point_a + point_b
distance = math.sqrt(result)

# display the result
print("The distance is", distance)
