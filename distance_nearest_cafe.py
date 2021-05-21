import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"{self.x}, {self.y}"


# https://www.mathsisfun.com/pythagoras.html
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))


P = [
    Point(2, 3),
    Point(12, 30),
    Point(40, 50),
    Point(5, 1),
    Point(12, 10),
    Point(3, 4)
]


# 1. Write a function that returns the distance from a given Point to all the points in the list P.
def calculate(P, p):
    distances = []
    # TODO cacculate and return distances
    for item in P:
        d = distance(p, item)
        distances.append(d)
    return distances


print(calculate(P, Point(20, 25)))


# OUTPUT [28.42534080710379, 9.433981132056603, 32.01562118716424, 28.30194339616981, 17.0, 27.018512172212592]

# EXTRA: Sort them and show their coordinates
def calculate_ordered(P, p):
    output = []
    # TODO cacculate and return distances
    for item in P:
        d = distance(p, item)
        output.append([d, item])
    return sorted(output)


house = Point(20, 25)
print(house)
print(calculate_ordered(P, house))
# OUTPUT [[9.433981132056603, 12, 30], [17.0, 12, 10], [27.018512172212592, 3, 4], [28.30194339616981, 5, 1], [28.42534080710379, 2, 3], [32.01562118716424, 40, 50]]


# EXTRA EXTRA PLOT THEM ON A GRID WITH NUMBERED MARKERS
# THE NEAREST STARBUCKS TO YOUR HOUSE ON A MAP

# CREATE EMPTY GRID
grid = []
for y in range(50):
    row = []
    for x in range(40):
        row.append('.')
    grid.append(row)
# REPLACE EMPTY DOTS WITH RANK ORDER FROM THE ORDERED FUNCTION
data = calculate_ordered(P, house)
grid[house.y - 1][house.x - 1] = "X"

counter = 1
for item in data:
    p = item[1]  # SECOND COLUMN AT INDEX 1 HAS THE POINT OBJECT
    grid[p.y - 1][p.x - 1] = counter
    counter += 1
# PRINT
for row in grid:
    for column in row:
        print(column, end=" ")
    print()
