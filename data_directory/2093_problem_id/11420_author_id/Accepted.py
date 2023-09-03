n,k = list(map(int,input().split()))
if k>n : print(-1); exit()
if k==1 and  n>1: print(-1); exit()
if k==1 and n==1: print('a'); exit()
s=''
f=1 
for i in range(n+2-k):
    s+='a' if f else 'b'
    f=1-f

c = ord('c')
for i in range(n+2-k,n):
    s+=chr(c)
    c+=1

print(s)