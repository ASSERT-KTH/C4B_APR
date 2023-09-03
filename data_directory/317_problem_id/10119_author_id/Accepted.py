n, a = map(int, input().split())
if a % 2 == 1 :
    print(int((a + 1) / 2))
else :
    print(int((n - a) / 2 + 1))