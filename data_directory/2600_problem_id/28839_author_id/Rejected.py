n=int(input())
R = lambda: map(int,input().split())
l= list(R())
l.sort()
print((n-1)//2)