rx = float(input("Enter reference x: "))
ry = float(input("Enter reference y: "))


n = int(input("Enter number of points: "))
points = []

for i in range(n):
    px = float(input("Enter x: "))
    py = float(input("Enter y: "))
    points.append([px, py])


size = len(points)

for i in range(size):
    min_index = i
    
    for j in range(i + 1, size):
        
        dx_j = points[j][0] - rx
        dy_j = points[j][1] - ry
        dist_j = (dx_j * dx_j) + (dy_j * dy_j)
        
        
        dx_min = points[min_index][0] - rx
        dy_min = points[min_index][1] - ry
        dist_min = (dx_min * dx_min) + (dy_min * dy_min)
        
        
        if dist_j < dist_min:
            min_index = j
            
    
    temp = points[i]
    points[i] = points[min_index]
    points[min_index] = temp


print("Sorted points:", points)
