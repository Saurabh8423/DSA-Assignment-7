def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x1) == 0:
            slope = float('inf')
        else:
            slope = (y - y1) / (x - x1)
        
        if (x - x2) == 0:
            prev_slope = float('inf')
        else:
            prev_slope = (y - y2) / (x - x2)
        
        if slope != prev_slope:
            return False

    return True
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(checkStraightLine(coordinates))  # Output: True
