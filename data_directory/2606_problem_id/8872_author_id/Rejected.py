al ="abcdefghijklmnopqrstuvwxyz"
size, distinct =map(int,input().split())
same =size-distinct+1
ans =""
for i in range(same):ans+=al[0]
size-=same
for i in range(1,size+1):ans+=al[i]
print (ans)