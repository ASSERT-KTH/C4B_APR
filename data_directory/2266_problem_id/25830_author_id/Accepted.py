n = int(input())

kid, count, res = 1, 1, []

for i in range(n-1):
    kid = (kid + count) % (n)
    res.append(n if kid == 0 else kid)
    count += 1

print(*res)