def read():
    return [int(x) for x in input().split()]
x,y=read()
i=0
while x<y:
    x*=3
    y*=2
    i+=1
print (i)