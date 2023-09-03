# A. Nearly Lucky Number
n = int(input())
s = str(n)
cnt4, cnt7 = 0, 0
for i in range(len(s)):
    if s[i] == '7':
        cnt7 += 1
    if s[i] == '4':
        cnt4 += 1
if cnt4 + cnt7 == 7 or cnt4 + cnt7 == 4:
    print("YES")
else:
    print("NO")