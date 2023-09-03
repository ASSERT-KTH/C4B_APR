def scan(type):
    return list(map(type, input().split()))
a,b,n, = scan(int)

a = str(a)
ans = -1

for i in range(10):
    temp = int(a + str(i))
    if (temp%b == 0):
        ans = str(temp) + (n-1)*'0'
print(ans)