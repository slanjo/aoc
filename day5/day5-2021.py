DELIMITER = "->"
import collections
from collections import namedtuple

if __name__ == '__main__':
    lines = []
    with open("/home/slanjo/Programming/aoc/day5/input.py", "r") as data_in:
        line = data_in.readlines()
        for string in line:
            lines.append(string.strip('\n').split(' -> '))

    OneLine = collections.namedtuple('OneLine', 'tocka1, junk, tocka2')
    print(line)
    print(len(line))
    print(lines)
    print(len(lines))

    for string in lines:
        string[0].split(',')
        string[1].split(',')

