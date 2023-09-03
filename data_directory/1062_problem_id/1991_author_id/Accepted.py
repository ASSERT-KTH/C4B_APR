s = input()
ans = 0
val = True
for a in s:
    if a == "7" or a == "4":
        ans = ans + 1
s = str(ans)
for a in s:
    if a == "7" or a == "4":
        ans = True
    else:
        ans = False
        break
if ans:
    print("YES")
else:
    print("NO")