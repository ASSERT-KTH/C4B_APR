n,a,b = input().split()
n,a,b = int(n),int(a),int(b)
if n - a>b+1:
    print(b+1)
else:
    print(n-a)