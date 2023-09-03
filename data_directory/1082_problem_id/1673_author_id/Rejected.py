k = int(input().strip())
l = int(input().strip())
jav = 0
while True:
    if l == 1:
        print('YES')
        print(jav-1)
        break
    elif l % k == 0:
        jav += 1
        l = l // k
    else:
        print('NO')