from os import read
from re import I
import numpy as np

draw = [42,44,71,26,70,92,77,45,6,18,79,54,31,34,64,32,16,55,81,
    11,90,10,21,87,0,84,8,23,1,12,60,20,57,68,61,82,49,59,22,2,
    63,33,50,39,28,30,88,41,69,72,98,73,7,65,53,35,96,67,36,4,51,
    75,24,86,97,85,66,29,74,40,93,58,9,62,95,91,80,99,14,19,43,37,
    27,56,94,25,83,48,17,38,78,15,52,76,5,13,46,89,47,3]

#draw = [16,38,19,24,29]  #first board
#draw = [28,13,34,45,37] #9th board horizontal
#draw = [0,75,86,55,58] #10th board horizontal
#draw = [3,58,90,93,96]  #last board horizontal
#draw  = [53,66,24,43,32 #""
#draw  = [62,84,19,82,22 #""
#draw  = [13,89,20,97, 1 #""
#draw  = [15,91,51,68,49 #""
#draw = [0, 13,7,10,16]
#draw = [20,11,10,24,4]
#draw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#input_matrix = np.genfromtxt("tickets-test.txt", dtype=int ) 
input_matrix = np.genfromtxt("tickets.txt", dtype=int)

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
                print(f"row[i] ----- {row[i]}")
            counter += 1
    return  

def process_tickets(input_matrix):
    
    input_len = len(input_matrix)
    row = 0
    board = 1 
    for board_start in range(0, input_len, 5):
        col_ticket = board_start
        ticket_arr = []
        column_arr = []
        for build_ticket in range(board_start, board_start + 5):
            ticket_arr = np.array(input_matrix[build_ticket])
            if is_win(ticket_arr) == 5:
                return board 
            row += 1
        row = 0
    
        for col in range(0, 5):
            for red in range(col_ticket, col_ticket + 5):
                column_arr.append(input_matrix[red][col])
            if is_win(column_arr) == 5:
                print("We have a winner")
                print(f"Column {col}, ticket {board}")
                return board
            column_arr = []
        board += 1 
    print("RETURNING -2")
    return -2

win_ticket = -2 
#k equls current draw
for k in draw:
    print(f"process_draw ===> {k}")
    process_draw(int(k), input_matrix) 
    print(f"input_matrix after process draw {k}\n{input_matrix}")
    win_ticket = process_tickets(input_matrix)
    print(win_ticket)
    if win_ticket != -2 and win_ticket != None:
        print(f"WIN TICKET = {win_ticket}")
        break

start_win_ticket = win_ticket * 5 - 5 
total = 0

for row in range (start_win_ticket, start_win_ticket + 5):
    for column in range (0, 5):
        if input_matrix[row][column] != -1:
            total += input_matrix[row][column]
print(f"K ====> {k}")
print(total * k)