s = input()
if len(s) != 4 and len(s) != 7:
    print("NO")
    exit()
for i in range(len(s)):
    if s[i] != '4' and s[i] != '7':
        print("NO")
        exit()
print("YES")