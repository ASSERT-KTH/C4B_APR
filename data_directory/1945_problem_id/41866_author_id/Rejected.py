def scan(type):
    return list(map(type, input().split()))
a,b,n, = scan(int)

a = str(a)

left = [(n,a)]
ans = -1

if (b == 1):
    print(a + '1'*(n-len(a)))
else:
    while (left):
        (n,a) = left.pop()
        if (n == 0):
            ans = a
            break

        for i in range(10):
            temp = int(a + str(i))
            if (temp%b == 0):
                left.append((n-1,str(temp)))
    print(ans)