a,b,c=input().split()
prvni,interval,jist=[int(a),int(b),int(c)]
if (jist >= prvni) and (jist!=prvni+1) and ((jist%(interval)==prvni) or (jist%(interval)==prvni+1)):
    print('YES')
else:
    print('NO')