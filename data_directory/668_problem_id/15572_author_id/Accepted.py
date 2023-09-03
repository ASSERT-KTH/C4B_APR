n=int(input())
S=''
for i in range(1,n+1):
    if i%2==0:
        S=S+'I love'
    else:
        S=S+'I hate'
    if i==n:
        S=S+' it '
    else:
        S=S+' that '
print(S)