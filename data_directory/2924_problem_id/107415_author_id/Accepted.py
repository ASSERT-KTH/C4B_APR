a = input()
b = input().split('0')
ans = [0]* len(b)
for i in range(len(b)):
    ans[i] = str(len(b[i]))

print(''.join(ans))