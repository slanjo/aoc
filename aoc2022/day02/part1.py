X = [ l.strip() for l in open('input.txt')]
win = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
lose = ['A Z', 'B X', 'C Y']
outcomes = {'A Y':8, 'B Z':9, 'C X':7, 'A X':4, 'B Y':5, 'C Z':6, 'A Z':3, 'B X':1, 'C Y':2}
#print(X)
total = 0
if __name__ == '__main__':
    for i in X:
        if i in outcomes:
            
            #            print(f"{outcomes[i]}")
        #        for (k, v) in outcomes:
        #    if i == k:
            total += outcomes[i]
    print(total)
                
                
            
