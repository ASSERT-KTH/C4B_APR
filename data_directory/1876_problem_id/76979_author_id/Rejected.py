##__________________________________________________________________
##
## Author:      GogolGrind
##__________________________________________________________________

from sys import *
from math import *

def main ():
    n = int(input())
    print ( '-1' if n < 3 else ('210' + '0' * (n-3)) )
if __name__ == '__main__':
    main()