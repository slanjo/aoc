ROW_LEN = 100
ROW_NUM = 100 

if __name__ == '__main__':
    in_string = []
    low_list = []
#   with open("test-in.txt", "r") as data:
    with open("input.txt", "r") as data:
        in_list = data.readlines()
        for string in in_list:
            in_string.append(string.strip('\n'))
     
    low_pos_dict = {}

    for row in range(len(in_string)):
#        print(len(in_string[i]))
        for col in range(len(in_string[row])):
            if col - 1 < 0 and row - 1 < 0:
                if int(in_string[row][col] < in_string[row][col + 1]):
                    if int(in_string[row][col] < in_string[row + 1][col]):
                        low_list.append(in_string[row][col])
                        low_pos_dict[] = f"{in_string[row][col]}"
            elif col - 1 < 0 and row + 1 == ROW_NUM:
                if int(in_string[row][col] < in_string[row][col + 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        low_list.append(in_string[row][col])
            elif col + 1 == ROW_LEN and row + 1 == ROW_NUM:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        low_list.append(in_string[row][col])
            elif col + 1 == ROW_LEN and row - 1 < 0:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row + 1][col]):
                        low_list.append(in_string[row][col])
            elif col - 1 < 0:
                if int(in_string[row][col] < in_string[row][col + 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        if int(in_string[row][col] < in_string[row + 1][col]):
                            low_list.append(in_string[row][col])
            elif col + 1 == ROW_LEN:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        if int(in_string[row][col] < in_string[row + 1][col]):
                            low_list.append(in_string[row][col])
            elif row - 1 < 0:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row][col + 1]):
                        if int(in_string[row][col] < in_string[row + 1][col]):
                            low_list.append(in_string[row][col])
            elif row + 1 == ROW_NUM:
                if int(in_string[row][col] < in_string[row][col - 1]):
                    if int(in_string[row][col] < in_string[row - 1][col]):
                        if int(in_string[row][col] < in_string[row ][col + 1]):
                            low_list.append(in_string[row][col])
            else: 
                try:
                    if int(in_string[row][col] < in_string[row][col - 1]):
                        if int(in_string[row][col] < in_string[row][col + 1]):
                            if int(in_string[row][col] < in_string[row + 1][col]):
                                if int(in_string[row][col] < in_string[row - 1][col]):
                                    low_list.append(in_string[row][col])
                except IndexError as index_num:
                    print(f"{index_num} is out of range on the last \'else\' ")
    print(low_list)
    risk_level = [ int(i) + 1 for i in low_list]
    print(sum(risk_level))
    print(low_pos_dict)