a,b,c=map(int,input().split())
x=c//a
s=2*c
for _ in range(x):
    s+=(c+1)
print(s)