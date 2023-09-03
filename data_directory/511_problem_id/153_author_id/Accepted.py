#n = int(input())
a, b, c = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
k = (a < b) * (c > 0) + (a > b) * (c < 0)
if a == b:
    print('YES')
else:
    if c == 0:
        print('NO')
    else:
        if (c == 0 and a == b) or (k and (b - a) % c == 0):
            print('YES')
        else:
            print('NO')