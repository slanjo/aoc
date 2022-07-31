#Jonathan Paulson
#https://www.youtube.com/watch?v=fHlWM8CIrlI

import sys
from collections import defaultdict, Counter

infile = sys.argv[1] if len(sys.argv) > 1 else '6.in' 

X = Counter([int(x) for x in open(infile).read().strip('\n').split(',')])
#print(f"N: {N}")
#X = defaultdict(int)
#X = {}
print(f"X: {X}")

#count elements of input by digit. a number of ones a number of twos
#and so on. this is better performed by Counter class. 
#for n in N:
#   if n not in X:
#       X[n] = 0
#   X[n]+=1

print(f"X after assignment: {X}")
def solve(S, n):
    X = S
    for day in range(n):
        Y = defaultdict(int)
        for x, cnt in X.items():
            print(f"day={day} | x={x} | cnt={cnt}")
            if x == 0:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x - 1] += cnt
        X = Y
    return(sum(X.values()))
print(solve(X, 1))
print("="*40)
print(solve(X, 80))
#print(solve(X, 256))

