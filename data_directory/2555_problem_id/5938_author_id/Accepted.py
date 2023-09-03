s = input()
res = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        res += 1
    else:
        res = 0
    if res >=6 :
        print("YES")
        break
else:
    print("NO")