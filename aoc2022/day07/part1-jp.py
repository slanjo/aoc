#Jonathan Paulson
from collections import defaultdict 
X=[]

#with open("input.txt", "r") as data:


if __name__ == '__main__':
    SZ = defaultdict(int) 
    path = []
    with open("input_t.txt", "r") as feed:
            data = feed.read().strip()
            lines = [x for x in data.split('\n')]
            #X.append(l.strip().split())

    
    for line in lines:
        words = line.strip().split()
        if  words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                #add directory name to dict as key:
                path.append(words[2]) 

        elif words[1] == 'ls':
            continue 

        elif words[0] == 'dir':
            continue
        else:
            sz = int(words[0]) 
            for k in range(1, len(path)+1):
                SZ['/]'.join(path[:k])] += sz
        print(path)
    p1 = 0
    p2 = 1e9
    for k, v in SZ.items():
        if v <= 100000:
            p1 += v
    print(SZ)
    print(p1)
    print(p2)
