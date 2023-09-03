n=int(input())
k=int(((2*n)**(1/2)))
while (k*(k+1))//2>=n:
    k-=1
print(n-(k*(k+1)//2))