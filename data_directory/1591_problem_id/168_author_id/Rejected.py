from math import ceil
i=int(input())
k=ceil(((2*i)-1)**0.5)
for j in range(k):
    if (j**2+1)/2>=i:
        print(j)
        break