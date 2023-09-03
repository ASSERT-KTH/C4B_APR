import math
s = input()
#list = s.split()
n = int(s.split()[0])
m = int(s.split()[1])
k = int( s.split()[2])
i = math.ceil(k/(2*m))
k-= (i-1)*2*m
j = math.ceil(k/(2))
if(k%2 ==1):
    print("%d %d L"%(i,j))
else:
    print("%d %d R" % (i, j))