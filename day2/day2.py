#Advent of Code 2021 day2
f = open("day2-in.txt", "r")
input_arr = f.readlines()

#print(input_arr)
horizontal_position = 0
depth = 0

for i in input_arr:
    x = i.split()
    if x[0] == "forward":
        horizontal_position += int(x[1])
    elif x[0] == "down":
        depth += int(x[1])
    elif x[0] == "up":
        depth -= int(x[1])

print(horizontal_position * depth)

##### Part two ######


horizontal_position = 0
depth = 0
aim = 0

for i in input_arr:
    x = i.split()
    if x[0] == "forward":
        horizontal_position += int(x[1])
        depth += (aim * int(x[1]))
    elif x[0] == "down":
        aim += int(x[1])
    elif x[0] == "up":
        aim -= int(x[1])

print(depth * horizontal_position)