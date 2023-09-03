def e_gcd(a,b):
    s = pt = 0
    ps = t = 1
    r = b
    pr = a
    while r:
        q = pr // r
        pr, r = r, (pr - q*r)
        ps, s = s, (ps - q*s)
        pt, t = t, (pt - q*t)
    return pr, (ps, pt)

a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]

g, x = e_gcd(a,c)
num = d - b
if num % g:         #if the difference cannot be bridged by multiples gcd
    print(-1)       #no solutions exist
else:
    u, v = x        #Take the Bezout id
    xp = num*u//g   #xp*a + yp*c == num, only interested in particular solution
    hs = c//g       #x incrmnt for homogeneous solution
    if not u:
        xp += num // g
    while xp > 0:
        xp -= hs
    while xp < 0:
        xp += hs
    ans = xp*a + b  #intersection
    if ans < d:
        o,p = e_gcd(a,c)
        while ans < d:
            ans += (a*c)//o
    print(ans)