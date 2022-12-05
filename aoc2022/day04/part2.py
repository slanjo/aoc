X = [l.strip().split(',') for l in open('input.txt')]

#X = [l.strip().split(',') for l in open('input_test.txt')]

if __name__ == '__main__':
    total = 0
    for i in X:
        list_a = [] 
        list_b = []
        first = i[0].split('-') 
        second = i[1].split('-') 

        a = int(first[0])
        b = int(first[1])

        for x in range(a, b+1):
            list_a.append(x)
        seta = set(list_a)
        if b:
            pass
        else:
            b = a

        c = int(second[0])
        d = int(second[1])

        for y in range(c, d + 1):
            list_b.append(y)

        setb = set(list_b)

        if seta.isdisjoint(setb):
            total += 1

        if d:
            pass
        else:
            d = c

        #if a > c:
            #if b <= d:
                ##add to total
                #total += 1 
        #elif a < c:
            #if b >= d:
                ##add to total
                #total += 1 
        #elif a == c:
            #if b <= d:
                ##add to total
                #total += 1 
            #elif b >= d:
                ##add to total
                #total += 1

    print(f"{len(X) - total}")
