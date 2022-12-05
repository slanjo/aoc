X = [l.strip().split(',') for l in open('input.txt')]

#X = [l.strip().split(',') for l in open('input_test.txt')]

if __name__ == '__main__':
    total = 0
    for i in X:

        first = i[0].split('-') 
        second = i[1].split('-') 

        a = int(first[0])
        b = int(first[1])
        
        if b:
            pass
        else:
            b = a
        c = int(second[0])
        d = int(second[1])
        if d:
            pass
        else:
            d = c

        if a > c:
            if b <= d:
                #add to total
                total += 1 
        elif a < c:
            if b >= d:
                #add to total
                total += 1 
        elif a == c:
            if b <= d:
                #add to total
                total += 1 
            elif b >= d:
                #add to total
                total += 1 

    print(f"{total}")
