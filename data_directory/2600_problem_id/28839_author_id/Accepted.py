n=int(input())
R = lambda: map(int,input().split())
l= list(R())
l.sort()
print(l[(n-1)//2])