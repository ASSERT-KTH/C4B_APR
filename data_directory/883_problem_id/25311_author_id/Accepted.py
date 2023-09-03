from collections import Counter

s = input()
z = set()

for i in range(len(s)):
    s = s[1:] + s[:1]
    z.add(s)

print(len(Counter(z)))