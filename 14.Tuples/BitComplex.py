# Complex Program: Distance between coordinate points stored in tuples

points = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    
    point = (x, y)
    points.append(point)

print("\nPoints entered:", points)

for i in range(len(points) - 1):

    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    print("Distance between", points[i], "and", points[i+1], "=", distance)
