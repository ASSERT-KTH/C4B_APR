s = input()
L = ['H','Q','9']
for i in range(len(s)):
    if s[i] in L:
        print("YES")
        exit()
print("NO")