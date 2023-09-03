a,b = map(int,input().split())
if(a==b and a==0):
    print("NO")
else:
    print("YES" if (abs(a-b)<=1) else "NO")