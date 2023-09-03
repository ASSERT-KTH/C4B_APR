x,y = map(int,input().split())
vol = x*y
if vol % 2 == 0: print(vol/2)
else:
    vol-=1
    print(vol/2)