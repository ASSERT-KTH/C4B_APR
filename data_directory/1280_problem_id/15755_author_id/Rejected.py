k = int(input())
a = input().split()
ans = 0
for i in range(len(a)) :
    a[i] = int(a[i])
for i in reversed(sorted(a)) :
    if k < 1 :
        print(ans)
        break
    k -= i
    ans += 1
else :
    print(-1)