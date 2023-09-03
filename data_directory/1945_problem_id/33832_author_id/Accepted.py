a, b, n = map(int,input().split())
g = False
for i in range(10):
    k = int(str(a) + str(i))
    if k % b == 0:
        g = True
        break
if g == True:
    final_len = n + len(str(a))
    remaining = final_len - len(str(k))
    print(k * 10 ** remaining)
else:
    print(-1)