import string
ALPHABET = string.ascii_lowercase + string.ascii_uppercase
ALPHADICT = {ALPHABET[i]:(i + 1) for i in range(len(ALPHABET))}

X = [l.split() for l in open("input.txt")]

def split_in_half(s, s1, s2):
    tally = 0
    for i in s[0]:
        if i in s1[0]:
            if i in s2[0]:
                return (ALPHADICT[i])
    return(0)

if __name__ == '__main__':

    total  = 0
    for s in range(0, len(X), 3):
        total += split_in_half(X[s], X[s + 1], X[s + 2])
    print(total)     

