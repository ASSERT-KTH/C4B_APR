p = input()

a=p[0]
cnt=1
for i in range(1, len(p)):
    if p[i] == a:
        cnt = cnt + 1
    else:
        a = p[i]
        cnt = 1
    if cnt == 7:
        print("YES")
        break

if i == len(p)-1 and cnt != 7:
    print("NO")