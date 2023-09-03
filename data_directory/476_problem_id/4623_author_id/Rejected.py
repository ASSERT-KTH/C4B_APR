##n = int(input())
##a = list(map(int, input().split()))
##print(" ".join(map(str, res)))

n = int(input())
res = n/3
res *= 2
if n%3 > 0:
    res += 1
print(res)