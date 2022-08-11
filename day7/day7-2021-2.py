#from aoc import get_input
import sys
import collections
MAKS = 1862
MAKS = 16
def sum_cost(start, stop):
    if start == stop:
        return 
    return( 

if __name__ == "__main__":
    f = sys.argv[1] if len(sys.argv) > 1 else '7.in'

    input_list = [int(x) for x in open(f).read().strip().split(",")]
    count = 0
    cost_list = []
    temp_list = []
    cost_dict = {}
    maks = 0 
    for i in input_list:
        if i > maks:
            maks = i

    grid_list = []


    print(f"Max value in input: {maks}")
    for hrzntl_pos_val in input_list:
        for indx in range(0,len(input_list)):
            temp_list.append(abs(hrzntl_pos_val - input_list[indx]))
        cost_dict[hrzntl_pos_val] = temp_list
        for key, value in cost_dict.items():
            for i in value:
                sum_cost(key, value)

        temp_list = []

    solution = 1_000_000_000_000_000_000_000_000 

    for key, value in cost_dict.items():
        total_new = 0
        for tally in value:
            total_new += tally 
        if total_new < solution:
            solution = total_new
#        print(f"key = {key}, list = {value} total = {total_new}")
        
        
    print(f"Solution: {solution}")
