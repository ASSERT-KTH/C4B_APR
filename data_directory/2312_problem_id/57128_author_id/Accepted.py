import math

s = input().split(' ');
h = int(s[0])
w = int(s[1])


ff = 2**math.floor(math.log2(h))
ss = 2**math.floor(math.log2(w))

if ff > ss :
    ff = min(ff, math.floor(ss*1.25))
else:
    ss = min(ss, math.floor(ff*1.25))


ff2 =  min(math.floor(ss*1.25), h)
ss2 =  min(math.floor(ff*1.25), w)

if ff*ss2>ss*ff2:
    print(ff, ss2)
else:
    print(ff2, ss)