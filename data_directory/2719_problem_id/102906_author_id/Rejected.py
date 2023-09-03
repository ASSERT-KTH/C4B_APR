ans = 0

rawInp = input().split(" ")
a, b = rawInp[0], rawInp[1]

while(a > b):
    a *= 3
    b *= 2
    ans += 1
print(ans)