from collections import OrderedDict
import string
ALPHABET = string.ascii_lowercase + string.ascii_uppercase
ALPHADICT = {ALPHABET[i]:(i + 1) for i in range(len(ALPHABET))}

X = [l.split() for l in open("input.txt")]

def split_in_half(s):
    tally = 0
    for ruck_item in s[0:(int(len(s) / 2))]: 
        if ruck_item in s[(int(len(s) / 2)): ]:
            tally = ALPHADICT[ruck_item]
    return(tally)

if __name__ == '__main__':

    total  = 0

    for s in X:
        total += split_in_half(s[0])
    print(total)     

