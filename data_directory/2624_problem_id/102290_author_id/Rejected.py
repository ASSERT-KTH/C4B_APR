n = int(input())
ans = ''

while(n >= 2):
    if (n >= 3):
        ans += '7'
        n-=3
    else:
        ans += '1'
        n-=2
print(ans)