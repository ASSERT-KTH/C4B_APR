import sys
from math import ceil
n,m,a = (int(x) for x in sys.argv[1:])
print (ceil(n/a) * ceil(m/a))