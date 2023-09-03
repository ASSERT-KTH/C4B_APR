k = int(input())
a = input().split()
ans = 0
for i in range(len(a)) :
    a[i] = int(a[i])
for i in reversed(sorted(a)) :
    if k < 1 :
        break
    k -= i
    ans += 1
if k < 1 :
    print(ans)
else :
    print(-1)