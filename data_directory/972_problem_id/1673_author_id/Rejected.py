n,m = map(int,input().split())
if max(n,m) - min(n,m) in {0,1} and n!= 0 and m != 0  :
    print('YES')
else:
    print("NO")