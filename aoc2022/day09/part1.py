from collections import defaultdict
X = [ l.strip() for l in open("input.txt")]
#X = [ l.strip() for l in open("input_t.txt")]

if __name__ == "__main__":
    walk = defaultdict(str)
    key = ()
    x, xt, y, yt = 0, 0,0, 0
    walk[0,0] = 'HT'
    for i in X:
        aim, dist = i.split()
        dist = int(dist)
        key = (x, y) 
        key_t = (xt, yt)
        print(f" {aim}:{dist} {key}, {key_t}")

        if aim == 'R':
            s = 0
            for k in range(x + 1, x + dist + 1):
                walk[k, y] += 'H'
                key = (k, y)
                if abs(k - xt) <= 1 and abs(y - yt) <= 1:
                    print("Right nothing") 
                elif abs(k - xt) >= 2 and abs(y - yt) >= 2:
                    yt = y
                    xt = k - 1
                    walk[xt, yt] += 'T'
                elif abs(k - xt) >= 2: #or abs(y - yt) >= 2:
                    yt = y
                    xt = k - 1
                    walk[xt, yt] += 'T'
                s = k
            x = s
        elif aim == 'U':
            s = 0
            for k in range(y + 1, y + dist + 1):
                walk[x, k ] += 'H'
                if abs(k - yt) <= 1 and abs(x - xt) <= 1:
                    print("Up do nothing")
                elif  abs(k - yt) >= 2 and abs(x - xt) >= 2:
                    xt = x 
                    yt = k - 1 
                    walk[(xt, yt)] += 'T'
                elif abs(k - yt) >= 2: 
                    xt = x
                    yt = k - 1 
                    walk[(xt, yt)] += 'T'
                s = k
            y = s
        elif aim == 'L':
            s = 0
            print(f"######  x,y {x},{y}  xt, yt {xt},{yt} ######")
            for k in range( x - 1, x - dist - 1, -1):
                walk[k, y ] += 'H'
                if abs(k - xt) <= 1 and abs(y - yt) <= 1:
                    print(f"left  nothing k={k}")
                if abs(k - xt) >= 2 and abs(y - yt) >= 2:
                    xt = k + 1
                    yt = y
                    walk[(xt, yt)] += 'T'
                elif  abs(k - xt) >= 2 or abs(y - yt) >= 2:
                    xt = k + 1
                    yt = y
                    walk[(xt, yt)] += 'T'
                s = k
            x = s
        elif aim == 'D':
            s = 0
            for k in range(y - 1, y - dist - 1, -1):
                walk[x, k] += 'H'
                if abs(k - yt) <= 1 and abs(x - xt) <= 1:
                    print("Down Nothing")
                elif abs(k - yt) >= 2 and abs(x - xt) >= 2:
                    xt = x 
                    yt = k + 1  
                    walk[xt, yt] += 'T'
                elif abs(k - yt) >= 2 or abs(x - xt) >= 2:
                    xt = x
                    yt = k + 1 
                    walk[(xt, yt)] += 'T'
                s = k
            y = s

    count = 0
    for k, v in sorted(walk.items()):
        count += 1
        print(count, k, v)

    answer = 0
    for k, v in walk.items():
        if 'T' in v:
            answer += 1
    print(f"Answer: {answer}")
