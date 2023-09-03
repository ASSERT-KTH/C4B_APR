t,s,x=map(int,input().split())
print('YES' if (x==t) or(x-t)%s==0 or((x-t-1)%s==0 and x!=t+1) else 'NO')