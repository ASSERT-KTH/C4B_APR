s = input()
df = 0
for k in range(1, len(s)):
    if s[k] == s[k - 1]:
        df += 1
        if df >= 7:
            break
    else:
        df = 0
if df >= 7:
    print('YES')
else:
    print('NO')