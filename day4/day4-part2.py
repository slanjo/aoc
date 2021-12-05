from os import read
from re import I
import numpy as np
from numpy.core.records import array

#draw = [42,44,71,26,70,92,77,45,6,18,79,54,31,34,64,32,16,55,81,
#    11,90,10,21,87,0,84,8,23,1,12,60,20,57,68,61,82,49,59,22,2,
#    63,33,50,39,28,30,88,41,69,72,98,73,7,65,53,35,96,67,36,4,51,
#    75,24,86,97,85,66,29,74,40,93,58,9,62,95,91,80,99,14,19,43,37,
#    27,56,94,25,83,48,17,38,78,15,52,76,5,13,46,89,47,3]
draw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
input_matrix = np.genfromtxt("tickets-test.txt", dtype=int ) 
#input_matrix = np.genfromtxt("tickets.txt", dtype=int)

def is_win(row):
    counter = 0
    for i in range(0, 5):
        if row[i] == -1:
            counter += 1
    return counter    

def process_draw(cur_draw, input_matrix):
    counter = 0
    for row in input_matrix:
        for i in range (0, len(row)): 
            if row[i] == cur_draw:
                row[i] = -1 
#                print(f"row[i] ----- {row[i]}")
            counter += 1
    return  

def process_tickets(input_matrix, current_draw):

    input_len = len(input_matrix)
    row = 0
    board = 1
    boards_aleady_won = [] 
    num_drawn = []
    tmp_num_drawn = []
    for board_start in range(0, input_len, 5):
        col_ticket = board_start
        ticket_arr = []
        column_arr = []
        for build_ticket in range(board_start, board_start + 5):
            ticket_arr = np.array(input_matrix[build_ticket])
            if board in boards_aleady_won:
                pass 
            else:
                if is_win(ticket_arr) == 5:
                    boards_aleady_won.append(board)
                    num_drawn.append(current_draw)
            row += 1
        row = 0
    
        for col in range(0, 5):
            for red in range(col_ticket, col_ticket + 5):
                column_arr.append(input_matrix[red][col])
            if board in boards_aleady_won:
                pass 
            else:
                if is_win(column_arr) == 5:
                    boards_aleady_won.append(board)
                    num_drawn.append(current_draw)
            column_arr = []
        board += 1 
    temp = []
    tmp_num_drawn = []
    for x in boards_aleady_won:
        if x not in temp:
            temp.append(x) 
    for y in num_drawn:
        if y not in tmp_num_drawn:
            tmp_num_drawn.append(y) 
#    print("RETURNING board")
    return temp, tmp_num_drawn

win_ticket = -2 
boards_won = []
tmp = []
arr_last_draw = []
k_temp = []
z = -1 
#all_boards = list(range(1,101))
#k equals current draw
all_boards = list(range(1,4))

for k in draw:
    for z in all_boards: 
        if z in boards_won:
            all_boards.pop(all_boards.index(z))
        elif z not in boards_won:
            process_draw(int(k), input_matrix) 
            cur_boards_won, k_temp = process_tickets(input_matrix, k)

            print(f"KTEMP -->>> {k_temp}")
            for i in cur_boards_won:
               if i not in boards_won:
                boards_won.append(i)
                print(boards_won)
            for s in k_temp:
                if s not in arr_last_draw:
                    arr_last_draw.append(s)

print(f"array_of_last_tables {boards_won}")
print(f"array last_draw  {arr_last_draw}")
last_board = boards_won.pop()
last_draw = arr_last_draw.pop()
print(f"last_board = {last_board}")
print(f"last_draw = {last_draw}")

board_start_row = last_board * 5 - 5 
total = 0
print(f"board starting row {board_start_row} total {last_board}  ")

print(f"{input_matrix}")
for redak in range (board_start_row, board_start_row + 5):
    for column in range (0, 5):
        if input_matrix[redak][column] != -1:
            total += input_matrix[redak][column]
print(total)
print(f"last drawn number {last_draw}")
print(total * last_draw)