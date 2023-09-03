p=[6,2,5,5,4,5,6,3,7,6]
a,b=map(int,input().split())
k=0
for i in range(a,b+1) :
    V=str(i)
    for j in range(len(V)) :
        k=k+p[int(V[j])]
print(k)