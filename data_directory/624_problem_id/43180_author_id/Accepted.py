a,b,c=input().split()
prvni,interval,jist=[int(a),int(b),int(c)]
if (jist >= prvni) and (jist!=prvni+1) and ((jist-prvni)%(interval)==0 or (jist-prvni-1)%(interval)==0):
    print('YES')
else:
    print('NO')