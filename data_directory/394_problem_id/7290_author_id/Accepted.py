n,m = [int(i) for i in input().split()]
if n%2 == 1:
    if m >= (n-1)/2:
        print (int((n-1)*n/2))
    else:
        t = (n-1)/2-m
        print (int((n-1)*n/2-t*(t*2+1)))
       
else:
    if m >= n/2:
        print (int((n-1)*n/2))
    else:
        t = n/2-m
        print (int((n-1)*n/2-t*(t*2-1)))