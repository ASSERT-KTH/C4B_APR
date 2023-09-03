'''
Created on

@author: linhz
'''
import sys
sys.setrecursionlimit(10000000)
usedNum=0
n=int(input())
p=[0 for i in range(n+1)]
used=[False for i in range(n+1)]
usedNum=0
def loop(i,num):
    global usedNum
    #print("i: %d num: %d usedNum: %d" %(i,num,usedNum))
    #print(p)
    if p[i]!=0 and p[i]!=num:
        return False
    else:
        if p[i]==0 and (not used[num]):
            p[i]=num
            used[num]=True
            usedNum+=1
            if loop(num,n-i+1):
                return True
            else:
                usedNum-=1
                used[num]=False
                p[i]=0
                return False
        elif p[i]==num:
            return True
        else:
            return False

if n%4==2 or n%4==3:
    print(-1)
else:
    i=1
    ansFlag=True
    while(usedNum<n and ansFlag):
        j=1
        flag=True
        while flag:
            while j<=n and used[j]:
                j+=1
            if(j<=n):
                #print("loop i=%d j=%d"%(i,j))
                if(loop(i,j)):
                    #print(p)
                    flag=False
                    break
                else:
                    j+=1
            else:
                ansFlag=False
                break
        i+=2
    ans=""
    for i in range(1,n+1):
        ans+=str(p[i])+" "
    if not ansFlag:
        ans="-1"
    print(ans)