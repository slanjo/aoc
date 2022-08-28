#Jonatha Paulson https://www.youtube.com/watch?v=DhQPrF-LBoE
#!/usr/bin/python3
import sys
from collections import defaultdict, Counter

if __name__ == '__main__':
    ans = 0
    f = sys.argv[1] if len(sys.argv) > 1 else '8.in'
    for line in open(f, "r"):
        before, after = line.split("|")
        before = before.split()
        after =  after.split()
        by_len = defaultdict(list)
        for w in before:
            by_len[len(w)].append(w)

        print(f"by_len = {by_len}")
        for w in after:
            if len(by_len[len(w)]) == 1:
                print(by_len[len(w)])
                ans += 1
#       print(by_len)
#    print(by_len)
    print(ans)
