t,s,x = map(int, input().split())
print('NO') if ((x-t)%s==0 or (x-t-1)%s==0) and x>=t+s or x==t else print('YES')