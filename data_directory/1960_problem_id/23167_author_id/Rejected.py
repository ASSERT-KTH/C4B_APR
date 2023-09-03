ans = 0
for i in range(5):
    a = ''.join(input().split())
    if a.find('1') > 0:
        ans = abs(i - 2) + abs(a.find('1') - 2)
print(ans)