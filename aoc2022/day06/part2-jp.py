#Jonathan Paulsen AoC 2022 Day06 
import sys
from copy import deepcopy
infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(infile).read()
test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz' 
test2 = 'nppdvjthqldpwncqszvftbrmjlhg' 
test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'




if __name__ == "__main__":
    p1 = False
    p2 = False

    for i in range(len(data)):
        if (not p1) and i - 3 >= 0 and len(set([data[i - j] for j in range(4)])) == 4:
            print(i + 1)
            p1 = True
        if (not p2) and i - 13 >= 0 and len(set([data[i - j] for j in range(14)])) == 14:
            print(i + 1)
            p2 = True

