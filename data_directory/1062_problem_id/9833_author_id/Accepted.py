def isLucky(n):
    count=0
    n1=n
    while n>0:
        r=n%10
        if r!=4 and r!=7:
            count+=1
            return False
        n=n//10
    if n1>0 and count==0:
        return True
    else:
        return False
def numdig(n):
    count=0
    while n>0:
        r=n%10
        if r==4 or r==7:
            count+=1
        n=n//10
    return count
n=int(input())
if isLucky(numdig(n)):
    print("YES")
else:
    print("NO")