DELIMITER = " -> "
#M = 10
#N = 10
M = 1000
N = 1000

ARR = [[0] * (N) for _ in range (M)]

import collections
from collections import namedtuple

def line_plot(x1y1, x2y2):
    x1 = x1y1[0]
    x2 = x2y2[0]
    y1 = x1y1[1]
    y2 = x2y2[1]

    x_direction = 1
    y_direction = 1

    if y1 > y2:
        biggery = y1
        smallery = y2
    elif y2 > y1:
        biggery = y2
        smallery = y1
    else:
        pass

    if x1 > x2:
        biggerx = x1
        smallerx = x2
    elif x2 > x1:
        biggerx = x2
        smallerx = x1
    else:
        pass
#    print(f"x1y1 = {x1y1}, x2y2 = {x2y2}")
    if abs(x1 - x2) == 0:
        x = x1
        for y in range(smallery, biggery + 1, 1):
                ARR[y][x] += 1

    elif abs(y1 - y2) == 0:
        y = y1
        for x in range(smallerx, biggerx + 1, 1):
                ARR[y][x] += 1

    elif (y1 -  y2) / (x1 - x2) == 1:
        print(f"SLOPE = {(y1 -  y2) / (x1 - x2)}\n -----------------")
        if x1 > x2 and y1 > y2:
            for x in range(x2, x1 + 1, 1):
                ARR[y2][x] += 1
                y2 += 1

        if x1 < x2 and y1 < y2:
            for x in range(x1, x2 + 1, 1):
                ARR[y1][x] += 1
                y1 += 1
###############
    elif (y1 -  y2) / (x1 - x2) == -1:
        print(f"SLOPE = {(y1 -  y2) / (x1 - x2)}\n -----------------")
        if x1 < x2 and y1 > y2:
            for x in range(x1, x2 + 1, 1):
                ARR[y1][x] += 1
                y1 -= 1

        if x1 > x2 and y1 < y2:
            for x in range(x2, x1 + 1, 1):
                ARR[y2][x] += 1
                y2 -= 1


        

if __name__ == '__main__':
    lines = []
#    with open("/home/slanjo/Programming/aoc/day5/test_input.txt", "r") as data_in:
    with open("/home/slanjo/Programming/aoc/day5/input.txt", "r") as data_in:
        line = data_in.readlines()
        for string in line:
            lines.append(string.strip('\n').split(DELIMITER))

    OneLine = collections.namedtuple('OneLine', 'tocka1, junk, tocka2')
    
    points = [] 
    for vent_line in lines:
        for vent_coordinate in vent_line:
            points.append(vent_coordinate.split(','))
    coordinates = []    
    for i in points:
        i[0] = int(i[0])
        i[1] = int(i[1])
        print(f"i = {int(i[0])}")
        for k in i:
            coordinates.append(int(k))
    
#   for i in coordinates:
#       if i > 900:
#           print(i)
    grid = []
#   for i in range(0, 1000):
#       for k in range(0, 1000):
#           grid.append(0)

    for i in range(0, 9):
        for k in range(0, 9):
            grid.append(0)
#Create a grid of M * N points)
    print(grid)
    print(f"(coordinates)\n {coordinates} \n, {len(coordinates)}")
    print(100*"*")
    print(f"lines\n {lines}")
    print(100*"*")
    print(f"points\n {points}\nLen of points = {len(points)}")
    print(100*"*")
    print(f"arr\n{ARR}")
    print(f"length of coordinates is {len(coordinates)}")
    for position in range(0, len(points), 2):
        line_plot(points[position], points[position+1])
#   for row in range(0, int(len(coordinates)/4)):
#       for col in range (0, 4):
#           print(coordinates[row][col])
    for line in ARR:
        print(line)
    total = 0
    for line in ARR:
        for item in line:
            if item >= 2:
                total += 1
    print(f"TOTAL = {total}")
    print("*" * 100)

