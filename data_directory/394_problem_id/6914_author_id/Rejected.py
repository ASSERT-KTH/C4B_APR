from sys import stdin
def input():
    return stdin.readline()


n,k=map(int,input().split())


ans=0
i=0
while i<k:
    ans+=n-i
    ans+=i
    i+=1

maxi=n*(n-1)//2
if ans>maxi:
    ans=maxi

print(ans)