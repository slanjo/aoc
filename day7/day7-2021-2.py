#from aoc import get_input
import sys
import collections
from recurse_hlpr import recurse_helper
MAKS = 1862
#MAKS = 16

if __name__ == "__main__":
    f = sys.argv[1] if len(sys.argv) > 1 else '7.in'

    print(f"RECURSION LIMIT {sys.getrecursionlimit()}")
    input_list = [int(x) for x in open(f).read().strip().split(",")]
    sys.setrecursionlimit(2000)
    count = 0
    cost_list = []
    temp_list = []
    cost_dict = {}
    cost_dict_2 = {}
    maks = 0 
    grid_list = []
    dist = 0
    cost_list_2 = []
    cost_2d = []
    print(f"Max value in input: {maks}")
    for crab in input_list:
        for indx in range(0,len(input_list)):
            temp_list.append(abs(crab - input_list[indx]))
        cost_dict[crab] = temp_list

#        for key, value in cost_dict.items():
#            for i in value:
#                
#                recurse_helper(MAKS)
        for indx in range(1, MAKS + 1):
#            dist = abs(crab - indx)
            cost = recurse_helper(abs(crab - indx))
            cost_list_2.append(cost)
        cost_dict_2[crab] = cost_list_2
        cost_2d.append(cost_list_2)
        cost_list_2 = []    

        temp_list = []
    solution1 = 1_000_000_000_000_000_000_000_000 

#    for crab, value in cost_dict_2.items():
#        print(f"{crab} --> {value}")

    for key, value in cost_dict.items():
        total_new = 0
        for tally in value:
            total_new += tally 
        if total_new < solution1:
            solution1 = total_new
#        print(f"key = {key}, list = {value} total = {total_new}")
        
    print(f"Solution part 1: {solution1}")
    for item in cost_2d:
        print(item)
    tally_list = []
    for col in range(MAKS):
        for row in range(len(cost_2d)):
            tally+=cost_2d[row][col]
        tally_list.append(tally)
        tally = 0
    i = 0
    n = 0
    for i in tally_list:
        if n >= i:
            n = i
    print(tally_list)
    print(f"solution2 = {min(tally_list)}")



