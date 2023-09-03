a=list(map(int, input().strip().split(' ')))
x=0
for i in a:
    x+=i
x=int(x/3)
d=0
for i in a:
    d+=abs(x-i)

print (d)