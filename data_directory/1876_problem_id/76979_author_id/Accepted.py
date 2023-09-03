##__________________________________________________________________
##
## Author:      GogolGrind
##__________________________________________________________________

from sys import *
from math import *

def mod (a,m):
    x = 0
    for i in reversed(a): 
        x = (x*10 + int(i)) % m
    r = []
    t = m - x
    while t > 0:
        r.append(t % 10)
        t //= 10
    return r
    
def main ():
    n = int(input())
    k = 2 * 3 * 5 * 7
    if (n < 3):
        print(-1)
        return 0
    elif (n == 3 ):
        print(k)
    else:
        t = [ 1 if i == 0 else 0 for i in range(n)]
        t = t[::-1]
        r = mod(t,k)        
        c = 0
        for i in range(len(r)):
            t[i] = r[i]
        for i in reversed(t):
            print(i, end = '')
                    
if __name__ == '__main__':
    main()