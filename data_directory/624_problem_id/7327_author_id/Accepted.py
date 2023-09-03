t,s,k = map(int, input().split())
if k<t or k-t==1:
    print("NO")
elif k==t:
    print("YES")
else:
    k -= t
    print("YES" if (k%s==0 or k%s==1) else "NO")