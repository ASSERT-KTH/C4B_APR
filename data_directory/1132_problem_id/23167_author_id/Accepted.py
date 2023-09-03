def isLucky(xx):
    x = xx

    ans = True
    while x > 0:
        if not(x%10 == 4 or x%10 == 7):
            ans = False
            break
        x = x//10
    return ans

n = int(input())
answer = False
for d in range(4, n+1):
   if n%d == 0 and isLucky(d):
       answer = True
       break
print('YES' if answer else 'NO')