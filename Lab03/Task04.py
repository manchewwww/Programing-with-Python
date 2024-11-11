# You are given an array coordinates, coordinates[i] = [x, y],
# where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/`

def checkStraightLine(coordinates):
    x1,y1, = coordinates[0]
    x2,y2 = coordinates[1]

    for i in range(2, len(coordinates)):
        x3, y3 = coordinates[i]
        determinant = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if determinant != 0:
            return False
    return True


print(checkStraightLine([[1, 2], [3, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
