s = input()
i = 0
count = 0
ans = False
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        count = count + 1

        if count == 7:
            ans = True
            break
    else:
        count = 0

    i = i + 1
if ans == True:
    print("YES")
else:
    print("NO")