al ="abcdefghijklmnopqrstuvwxyz"
size, distinct =map(int,input().split())
ans =""
i =0
while size > 0:
    ans+=al[i]
    i+=1
    if i == distinct: i =0
    size-=1
print (ans)