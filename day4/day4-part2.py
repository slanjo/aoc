#2 * \n in python is a blank line
import collections
#DRAW_NUMS = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
DRAW_NUMS = [42,44,71,26,70,92,77,45,6,18,79,54,31,34,64,32,16,55,81,11,90,10,21,87,
            0,84,8,23,1,12,60,20,57,68,61,82,49,59,22,2,63,33,50,39,28,30,88,41,69,
            72,98,73,7,65,53,35,96,67,36,4,51,75,24,86,97,85,66,29,74,40,93,58,9,62,
            95,91,80,99,14,19,43,37,27,56,94,25,83,48,17,38,78,15,52,76,5,13,46,89,47,3]
BOARDS = [] # A list condaining all boards before the game starts
BOARDS_WON = [] # A list of boards containing bord numbers of the boards that have won 
TRACK_BOARDS = []  # A list to be used to mark all draws on a board, mark a draw with -1


def find_board(board, drawn_num):

    board_first_row = board * 5 - 5
    board_last_row = board_first_row + 5
    if not has_won(board):
        for row in range (board_first_row, board_last_row):
            for col in range(0, 5):
                if drawn_num == int(BOARDS[row][col]):
                    print(f"board #: {board}, Position: ({row % 5, col})")
                    #set row/col in TRACK_BOARDS list to -1
                    TRACK_BOARDS[row][col] = -1
                    LAST_NUM.append(drawn_num)
                    return board 
    else:        
        if has_won(board) and board not in BOARDS_WON:
            BOARDS_WON.append(board) 
            return None

def has_won(board):
    count_h = 0
    count_v = 0
    board_first_row = board * 5 - 5
    board_last_row = board_first_row + 5
    #Check winning rows
    for row in range(board_first_row, board_last_row):
        for col in range(0, 5):
            if int(TRACK_BOARDS[row][col]) == -1:
                count_h += 1    
        if count_h == 5:
            return True
        else:
            count_h = 0

    #Check winning columns
    for col in range(0, 5):
        for row in range(board_first_row, board_last_row):
            if int(TRACK_BOARDS[row][col]) == -1:
                count_v += 1    
        if count_v == 5:
                return True
        else:
            count_v = 0

    return False

if __name__ == '__main__':

    # PREPARE BOARDS
#    with open("tickets-test.txt", "r") as data_file:
    with open("tickets.txt", "r") as data_file:
        data = data_file.read().splitlines()
        temp = [line.split("\n") for line in data] 
    char_list = [] 
    data = []
    for line in temp:
        for char in line:
            if char != '':
                char_list.append(char)
    for line in char_list:
        BOARDS.append(line.split())
    TRACK_BOARDS = BOARDS
    boards_count = int(len(BOARDS)/5)
    print(f"Length of BOARDS: {len(BOARDS)}. Number of boards: {boards_count}")
    LAST_NUM = []
    # RUN GAME
    for drawn_num in DRAW_NUMS:
        if len(BOARDS_WON) < boards_count:
            for board in range(1, boards_count + 1):
                if board in BOARDS_WON:
                    print(f"Board {board} has already won")
                else:
                    print(f"Found {drawn_num} on board num: {find_board(board, drawn_num)}")

                #if call to check_boards for a drawn_num returns True
                #call a function to check if the board has won
                #if the board has one and is in the won_boards list pass
                #if the board has won and is not in the WON_BOARDS list add the board_number to the WON_BOARDS list 
    suma = 0
    int_track_boards = []
    print(TRACK_BOARDS)
    print(f"The last drawn number is {LAST_NUM[-1]}, the last winning board is {BOARDS_WON[-1]}")

    
            
    board_first_row = BOARDS_WON[-1] * 5 - 5
    board_last_row = board_first_row + 5
    for row in range (board_first_row, board_last_row):
        for col in range(0, 5):
            if int(TRACK_BOARDS[row][col]) != -1:
                suma += int(TRACK_BOARDS[row][col])
            
    print(f"REUSLT: {suma * LAST_NUM[-1]}")
