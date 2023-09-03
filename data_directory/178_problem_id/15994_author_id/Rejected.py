l,r,k = [int(i) for i in input().split()]
i = 0
while True :
    t = k ** i
    if t <=r and t >=l:
        print(t,end=" ")
    else:
        break
    i+=1