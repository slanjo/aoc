import sys


def recurse_helper(n):
    if n <= 1:
        return(n)
    else:
        return n + recurse_helper(n - 1)

if __name__ == '__main__':
    f = sys.argv[1] if len(sys.argv[1]) > 1 else '7r.in'

#    print(f"zbroj = {recurse_helper(4)}") 
