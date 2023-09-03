def gcd(a,b):
    if a==0:
        return int(b)
    return int(gcd(b%a,a))

t,w,b=map(int,(input().split()))

lcm = int((w*b)/gcd(w,b))
mul = int(t//lcm)
ans = min(t, lcm*mul+int(min(w,b)-1)) - lcm*mul + 1
ans += mul*min(w, b) - 1
g2 = gcd(ans,t)
print(int(ans/(g2)),"/",int(t//(g2)),sep="")