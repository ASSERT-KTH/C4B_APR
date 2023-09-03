a, b, n = map(int,input().split())
for i in range(10):
    k = int(str(a) + str(i))
    if k % b == 0:
        break
final_len = n + len(str(a))
remaining = final_len - len(str(k))
print(k * 10 ** remaining)