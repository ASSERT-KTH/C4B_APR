n = int(input())


def r(n):
    i = 0
    high = 20000000
    low = 0

    while low +2 < high :
        mid = (high + low) // 2
        #print(low, high, mid)
        a = mid*(mid+1)//2
        b = (mid+1)*(mid+2)//2
        #print(a,b,n)
        if a <= n < b :
            break
        elif a < n :
            low = mid
        else :
            high = mid + 1

    x = n-mid*(mid+1)//2+1
    return x

if n == 1 :
    print(1)
else:
    print(r(n-1))