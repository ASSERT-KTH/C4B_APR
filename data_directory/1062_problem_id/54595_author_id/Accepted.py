s = input()
tmp = 0
for i in range(len(s)):
    if s[i] == '4' or s[i] == '7':
        tmp += 1
if tmp == 4 or tmp == 7:
    print("YES")
else:
    print("NO")