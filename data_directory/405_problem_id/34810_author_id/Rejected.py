x = int(input())
c = 0
while(x>0):
    d = x % 8
    print(d)
    c += (d == 1)
    x = x // 8
print(c)