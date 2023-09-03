n = int(input())
if n == 2:
    print(3)
else:
    ans = n // 2 + 1
    n %= 4
    if n and not(ans & 1):
        ans += 1
    if n > 1 and ans <= 3:
        ans += 2
    print(ans)