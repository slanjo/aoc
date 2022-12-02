X = [ l.strip() for l in open('input.txt')]
WIN = ['C 1', 'A 2', 'B 3']
DRAW = ['A 1', 'B 2', 'C 3']
LOSE = ['A 3', 'B 1', 'C 2']

def find_outcome(opponent_outcome, round_outcome):
    if round_outcome == 'l': #lose
        for l in LOSE:
            if l[0] == opponent_outcome:
                return int(l[2]) + 0

    elif round_outcome == 'd': #draw
        for l in DRAW:
            if l[0] == opponent_outcome:
                return int(l[2]) + 3

    elif round_outcome == 'w': #win
        for l in WIN:
            if l[0] == opponent_outcome:
                return int(l[2]) + 6
    return 0

total = 0
if __name__ == '__main__':
    for i in X:

        if i[2] == 'X': #lose
            total += find_outcome(i[0], 'l') 

        elif i[2] == 'Y': #draw
            total += find_outcome(i[0], 'd') 

        elif i[2] == 'Z': #win
            total += find_outcome(i[0], 'w') 

    print(total)
                
                
            
