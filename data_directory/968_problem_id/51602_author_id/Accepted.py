m,d = list(map(int, input().split()))
if m == 4 or m == 6 or m == 9 or m == 11:
    n = 30
elif m == 2:
    n = 28
else:
    n = 31
if m == 2 and d == 1:
    print(4)
elif n == 30 and d == 7:
    print(6)
elif n == 31 and(d == 6 or d == 7):
    print(6)
else:
    print(5)