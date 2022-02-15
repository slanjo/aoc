#from pandas import *


#ROW_LEN = 100
#ROW_NUM = 100 
ROW_LEN = 10
ROW_NUM = 5 

if __name__ == '__main__':
    in_string = []
    low_list = []
    line_chars = []
    grid = []
    with open("test-in.txt", "r") as data:
#    with open("input.txt", "r") as data:
        in_list = data.readlines()
        for string in in_list:
            in_string.append(string.strip('\n'))
            line_chars = [letter for letter in string if letter != '\n']
            grid.append(line_chars) # line_chars is a list of characters in one line
         
    low_pos_dict = {}
    grid_dict = {}
    for row in range(len(in_string)):
#        print(len(in_string[i]))
        for col in range(len(in_string[row])):
            #temp_dict ={f"{row},{col}":in_string[row][col]} 
            temp_dict ={(row,col):int(in_string[row][col])} 
            grid_dict.update(temp_dict)
            if col - 1 < 0 and row - 1 < 0:
                if int(in_string[row][col] < in_string[row][col + 1]):
                    if int(in_string[row][col] < in_string[row + 1][col]):
                        low_list.append(in_string[row][col])
                        low_pos_dict.update(temp_dict)
            elif col - 1 < 0 and row + 1 == ROW_NUM:
                if int(in_string[row][col] < in_string[row][col + 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        low_list.append(in_string[row][col])
                        low_pos_dict.update(temp_dict)
            elif col + 1 == ROW_LEN and row + 1 == ROW_NUM:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        low_list.append(in_string[row][col])
                        low_pos_dict.update(temp_dict)
            elif col + 1 == ROW_LEN and row - 1 < 0:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row + 1][col]):
                        low_list.append(in_string[row][col])
                        low_pos_dict.update(temp_dict)
            elif col - 1 < 0:
                if int(in_string[row][col] < in_string[row][col + 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        if int(in_string[row][col] < in_string[row + 1][col]):
                            low_list.append(in_string[row][col])
                            low_pos_dict.update(temp_dict)
            elif col + 1 == ROW_LEN:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        if int(in_string[row][col] < in_string[row + 1][col]):
                            low_list.append(in_string[row][col])
                            low_pos_dict.update(temp_dict)
            elif row - 1 < 0:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row][col + 1]):
                        if int(in_string[row][col] < in_string[row + 1][col]):
                            low_list.append(in_string[row][col])
                            low_pos_dict.update(temp_dict)
            elif row + 1 == ROW_NUM:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        if int(in_string[row][col] < in_string[row ][col + 1]):
                            low_list.append(in_string[row][col])
                            low_pos_dict.update(temp_dict)
            else: 
                try:
                    if int(in_string[row][col] < in_string[row][col - 1]):
                        if int(in_string[row][col] < in_string[row][col + 1]):
                            if int(in_string[row][col] < in_string[row + 1][col]):
                                if int(in_string[row][col] < in_string[row - 1][col]):
                                    low_list.append(in_string[row][col])
                                    low_pos_dict.update(temp_dict)
                except IndexError as index_num:
                    print(f"{index_num} is out of range on the last \'else\' ")
    print(low_list)
    risk_level = [ int(i) + 1 for i in low_list]
    print(sum(risk_level))
    print(low_pos_dict)
#    xy = 26
    xy = 5
#    print(grid_dict[(99,xy)])
    print(grid_dict[(4,xy)])
    print(f"low-position-dict:::::{low_pos_dict}")
    print(f"single line character list (used for check): -------\n{line_chars}\n-----------")
    #print(in_list)
    print(50 * "-" + f"\nGrid: \n{grid}\n" + 50 *"-")
    print(f"lenght of Grid list: {len(grid)}")

    for (key, value) in low_pos_dict.items():
        print(f"{key[0]},{key[1]}")
        print(key)
        print(f"Value of the low point in the grid at the current coordinates: {grid[key[0]][key[1]]}")