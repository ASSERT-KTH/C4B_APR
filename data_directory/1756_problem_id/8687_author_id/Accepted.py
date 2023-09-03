s = list(map(int, input().split()))
se = set()
for i in range(len(s)):
    se.add(s[i])
print(4 - len(se))