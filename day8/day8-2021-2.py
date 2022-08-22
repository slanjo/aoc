import sys
from collections import defaultdict, Counter


if __name__ == '__main__':
    X = []
    f = sys.argv[1] if len(sys.argv) > 1 else '8.in'
#    with open("test.in", "r") as f:
#        lista = f.read().splitlines()
#    X = lista
    counter = 0
    X = [x for x in open(f).read().splitlines()]
    Y = []
    for y in X:
        Y.append(y.split('|'))
    for tally in Y:
        counter_lst = tally[1].split(' ')
        for i in counter_lst:
            if len(i) in (2, 4, 3, 7): 
                counter+=1

    print(f"Total = {counter}")
