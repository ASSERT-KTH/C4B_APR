import sys
n,k = input().split()
n=int(n)
k=int(k)
s=""
x=k
for i in range(n):
    if k>0:
        s=s+chr(97+i)
        k-=1
    else:
        for j in range(x):
            s=s+chr(97+j)
            j+=1
            if len(s)==n:
                print(s)
                sys.exit()
print(s)