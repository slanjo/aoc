'''Advent of code 2021 Day 1'''
from os import terminal_size


f = open("da1-test-in.txt", "r")
f = open("day1-in.txt", "r")

txt_input = f.readlines()

num_input = []
count_increased = 0


for i in txt_input:
    num_input.append(int(i))


for i in range(1, len(num_input) - 1):
    print(f"element {i} is {num_input[i]}") 
    if num_input[i]  > num_input[i - 1]:
        count_increased += 1
        print(f"counter = {count_increased}==== i is {i}")

if num_input[len(num_input) - 1] >  num_input[len(num_input) - 2]:
    count_increased += 1

print(count_increased)

### ||| part two |||

#print(txt_input)
#print(num_input)


suma = []
for i in range(2, len(num_input) - 1):
    suma.append(num_input[i] + num_input[i - 1] + num_input[i - 2])
suma.append(num_input[-1] + num_input[-2] + num_input[-3] )
print(f"-------------------- last element{suma[len(suma) -1]}")
print(suma)
count_increased_suma = 0
for x in range(1, len(suma) - 1):
    print(f"element {x} is {suma[x]}") 
    if suma[x]  > suma[x - 1]:
        count_increased_suma += 1
        print(f"counter = {count_increased_suma}==== i is {x}")

if suma[len(suma) - 1] >  suma[len(suma) - 2]:
    count_increased_suma += 1

print(count_increased_suma)