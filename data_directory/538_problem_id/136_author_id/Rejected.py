A=[int(i) for i in input().split()]
z=sum(A)
d=z
for i in range(len(A)):
    if A.count(A[i])>=2:
        h=z-A.count(A[i])*A[i]
        if h<d:
            d=h
print(d)