n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True)
c,d,x=0,-1,0
for i in range(12):
    c=c+1;x=x+s[i]
    if x>=n:
        d=1
        break;
  
if d>0 :print(c)
else :
    print( 0 if n==0  else -1)