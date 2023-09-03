s = input()
length = len(s)

miss = 0
for i in range(0, length//2):
    if s[i] != s[length-1-i]:
        miss += 1

if miss == 1:
    print('YES')
else:
    print('NO')