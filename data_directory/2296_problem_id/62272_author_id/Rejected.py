(m, n,) = list(map(int, input().split()))

if m%2 != 0 and n%2 != 0 and m != 1 and n != 1:
    ans = (((m*(n-1))/2)+1)
elif m == 1 and n%2 == 0:
    ans = n/2
elif n == 1 and m%2 == 0:
    ans = m/2
elif n == 1 and m%2 != 0:
    ans = (m-1)/2
elif m == 1 and n%2 != 0:
    ans = (n-1)/2
elif (m == 1) and (n == 1):
    ans = 0
else:
    ans = ((m * n) / 2)

print (int(ans))