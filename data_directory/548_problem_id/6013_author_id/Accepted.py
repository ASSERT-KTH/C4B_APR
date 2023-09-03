n,m=map(int,input().split())
print(sum((m+((i+1)%5))//5 for i in range(n)))