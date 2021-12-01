'''Advent of code 2021 Day 1'''

from os import terminal_size


f = open("da1-test-in.txt", "r")
f = open("day1-in.txt", "r")

txt_input = f.readlines()

num_input = []
count_increased = 0


for i in txt_input:
    num_input.append(int(i))


for i in range(1, len(num_input)):
    if num_input[i]  > num_input[i - 1]:
        count_increased += 1

print(count_increased)

### ||| part two |||


suma = []
for i in range(2, len(num_input)):
    suma.append(num_input[i] + num_input[i - 1] + num_input[i - 2])

count_increased_suma = 0
for x in range(1, len(suma)):
    if suma[x]  > suma[x - 1]:
        count_increased_suma += 1

print(count_increased_suma)
