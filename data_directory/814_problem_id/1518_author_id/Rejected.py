m=list(map(int, input().split(' ')))
p=m[0]
r=m[1]
if(p%10==0):
    print(1)
elif(p%10==r):
    print("1")
elif(p%10==5):
    print("2")
else:
    c=1
    while(1):
        x=p*c
        if(x%10==r):
            print(c)
            break
        c+=1