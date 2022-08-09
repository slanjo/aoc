#from aoc import get_input
import sys

if __name__ == "__main__":
    f = sys.argv[1] if len(sys.argv) > 1 else '7.in'
#    data = get_input(1).splitlines()

    moja_lista = [int(x) for x in open(f).read().strip().split(",")]

    
