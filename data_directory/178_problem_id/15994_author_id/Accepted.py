l,r,k = [int(i) for i in input().split()]
i = 0
g=True
while True :
    t = k ** i
    if t <=r and t >=l:
        g=False
        print(t,end=" ")
    elif t > l:
        break
    i+=1
if g:
    print(-1)