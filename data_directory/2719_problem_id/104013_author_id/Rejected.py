i = lambda:map(int,input().split())
a,b = i()
c = 0
while a < b:
    a = a*3
    b = b*2
    c = c+1
print(c)