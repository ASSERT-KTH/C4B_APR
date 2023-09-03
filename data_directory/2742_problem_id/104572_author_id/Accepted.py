n=int(input())
k=int(n/2)-1
if n-k*2==3:
    print(7,end='')
else:
    print(1,end='')
for i in range(k):
    print(1,end='')