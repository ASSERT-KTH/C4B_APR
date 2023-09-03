n,a,b,c = input().split()
n,a,b,c =int(n),int(a),int(b),int(c)
A = []
A.append(a)
A.append(b)
A.append(c)
A.sort()
d = n%A[0]
while d%b != 0:
    d = d+a