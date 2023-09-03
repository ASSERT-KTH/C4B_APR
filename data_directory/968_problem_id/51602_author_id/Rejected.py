m,d = list(map(int, input().split()))
if m == 2 and d == 1:
    print(4)
elif m == 2:
    print(5)
elif d == 5 or d == 6 or d == 1:
    print(5)
else:
    print(6)