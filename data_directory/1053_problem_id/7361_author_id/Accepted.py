n = int(input())
f,s = n//7,0;
ans = -1
for i in range(f,-1,-1):
    if (n-7*i)%4==0:
        ans=i;
        break;
if ans==-1:
    print(-1);
else:
    print('4'*((n-7*ans)//4)+'7'*ans)