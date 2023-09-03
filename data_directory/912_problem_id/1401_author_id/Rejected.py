C = list(map(int, input().split()))
if sum(C) == 0:
    print(-1)
elif sum(C) % 5 == 0:
    print(sum(C) // 5)
else:
    print(-1)