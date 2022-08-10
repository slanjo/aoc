#from aoc import get_input
import sys

if __name__ == "__main__":
    f = sys.argv[1] if len(sys.argv) > 1 else '7.in'
#    data = get_input(1).splitlines()

    input_list = [int(x) for x in open(f).read().strip().split(",")]
    count = 0
#    print(input_list) 
    cost_list = []
    temp_list = []
    cost_dict = {}
    position = 0
    for hrzntl_pos_val in input_list:
        for indx in range(0,len(input_list)):
            temp_list.append(abs(hrzntl_pos_val - input_list[indx]))
        cost_dict[hrzntl_pos_val] = temp_list
#        cost_dict[position] = temp_list
        temp_list = []
        position+=1
    solution = 1_000_000_000_000_000_000_000_000 
    for key, value in cost_dict.items():
        total_new = 0
        for tally in value:
            total_new += tally 
        if total_new < solution:
            solution = total_new
        print(f"key = {key}, list = {value} total = {total_new}")
        
        
    print(solution)
