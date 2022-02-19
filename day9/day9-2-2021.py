#from pandas import *
# used graph reference: 
# https://www.redblobgames.com/pathfinding/GRIDs/graphs.html
# https://www.redblobgames.com/pathfinding/a-star/implementation.html

ROW_LEN = 100
ROW_NUM = 100 
#ROW_LEN = 10
#ROW_NUM = 5 
GRID = []
NEIGHBOR_LIST = []
ALL_NODES = []

def find_neighbors(node, node_value, result):
    directions = [[1,0], [0,1], [-1,0], [0,-1]] 
    for drctn in directions:
        neighbor = [node[0] + drctn[0], node[1] + drctn[1]]
        if neighbor in ALL_NODES: 
            if int(GRID[int(neighbor[0])][int(neighbor[1])]) > int(node_value):
                if int(GRID[int(neighbor[0])][int(neighbor[1])]) < 9:
                    neighbor_value = int(GRID[int(neighbor[0])][int(neighbor[1])]) 
                    if neighbor not in result:
                        result.append(neighbor)
                        find_neighbors(neighbor, neighbor_value, result)
    return len(result) + 1
    print(f"NEIGHBOR_LIST ---- {NEIGHBOR_LIST}\n")
#        if 0 <= neighbor[0] < ROW_NUM and 0 <= neigbor[1] < ROW_LEN:
if __name__ == '__main__':
    for x in range(ROW_NUM):
        for y in range(ROW_LEN):
            ALL_NODES.append([x, y])
    in_string = []
    low_list = []
    line_chars = []
#    grid = []
#    with open("test-in.txt", "r") as data:
    with open("input.txt", "r") as data:
        in_list = data.readlines()
        for string in in_list:
            in_string.append(string.strip('\n'))
            line_chars = [letter for letter in string if letter != '\n'] #generating a list of characters so we can assign positions/locations to them
            GRID.append(line_chars) # line_chars is a list of characters in one line, 
                                    # grid then becomes a 2D array (a list of line lists) containing our graph values
         
    low_pos_dict = {}
    grid_dict = {}
    for row in range(len(in_string)):
#        print(len(in_string[i]))
        for col in range(len(in_string[row])):
            #temp_dict ={f"{row},{col}":in_string[row][col]} 
            temp_dict ={(row,col):int(in_string[row][col])}  #create a dict containing position and a value of position for 
                                                             # each node. It is a tuple:value format - {(0, 1): 1}
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
    print(f"start of low_list {low_list} \n END OF low_list")
    risk_level = [ int(i) + 1 for i in low_list]
    print(f"risk_level: {sum(risk_level)}")
#   column = 26
    column = 5
#    print(grid_dict[(99,column)])
    print(f"GRID DICT row: 4, culumn: {column} value: {grid_dict[(4,column)]}")
    print(f"low-position-dict:::::{low_pos_dict}")
    print(f"last line in our GRID (used for check): -------\n{line_chars}\n-----------")
    #print(in_list)
    print(50 * "-" + f"\nGrid: \n{GRID}\n" + 50 *"-")
    print(f"lenght of Grid list: {len(GRID)}")
    low_pos_list = []
    for (key, value) in low_pos_dict.items():
        print(f"{key[0]},{key[1]}")
        low_pos_list.append([key[0],key[1]]) # Generate a list of los positions, to feed into graph search
        print(key)
        print(f"Value of the low point in the GRID at the current coordinates: {GRID[key[0]][key[1]]}")
    print(low_pos_list)
    cluster_size = 0
    result_list = []
    for item in low_pos_list:
        result = []
        cluster_size = find_neighbors(item, GRID[ item[0] ] [item[1] ], result) 

        print(f"NODE: {item} VALUE: {GRID[ item[0] ] [item[1] ]}, CLUSTER SIZE: {cluster_size}")
    
        result_list.append(cluster_size)    
    result_list.sort()
    lista = result_list
    print(lista)
    lista.sort(reverse=True)
    print(lista)
    print(lista[0] * lista[1] * lista[2])