s = input()
ans = True
for a in s:
    if a == "7" or a == "4":
        continue
    else:
        ans = False
        break
if ans:
    print("YES")
else:
    print("NO")