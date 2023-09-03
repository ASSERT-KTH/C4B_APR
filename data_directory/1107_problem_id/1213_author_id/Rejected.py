a,b,n = input().split()
a = int(a)
b = int(b)
n = int(n)
count = 1
    
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b )
while n > -1:
    x = gcd(a, n)
    if n >=x:
        n = n - x
    else:
        conut = 1
        break
    
    x = gcd(b, n)
    if n >=x:
        n = n - x
    else:
        count = 2
        break
    print(n)
print(count)
if count == 1:
    print('1')
else:
    print('0')