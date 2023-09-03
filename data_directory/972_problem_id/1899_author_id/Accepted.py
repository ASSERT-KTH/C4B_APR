n, k = [int(i) for i in input().split()]
if abs(n-k)<=1:
    if n==k==0:
        print ('NO')
    else:
        print ('YES')
else:
    print ('NO')