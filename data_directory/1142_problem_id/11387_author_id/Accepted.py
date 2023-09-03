n,a,b = input().split()
n,a,b = int(n),int(a),int(b)

if (a+b >= n):
    if (n-a >= 0):
        print(n-a)
    else:
        print(0)
else:
    print(b+1)