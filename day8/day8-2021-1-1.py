#!/usr/bin/python3.10
import sys
from collections import defaultdict, Counter

if __name__ == '__main__':

    f = sys.argv[1] if len(sys.argv) > 1 else '8.in'
    for line in open(f, "r"):
        before, after = line.split("|")
        
        print(after)
