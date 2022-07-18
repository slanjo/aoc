import collections
#from collections import namedtuple

if __name__ == '__main__':
    lines = []
    with open("/home/slanjo/Programming/aoc/day5/input.txt", "r") as data_in:
        line = data_in.readlines()
        for string in line:
            lines.append(string.strip('\n'))

    OneLine = collections.namedtuple('OneLine', 'tocka1, junk, tocka2')
    for tocka in map(OneLine._make, "input.txt"):
        print(tocka.tocka1, tocka.tocka2)
    print(line)
    print(len(line))
    print(lines)
    print(len(lines))
