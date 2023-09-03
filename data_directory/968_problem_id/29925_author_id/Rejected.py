import math
m,d = [int(i) for i in input().split()]
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
al = mon[m-1]
weeks = math.ceil((al-(7-d+1))/7) + 1