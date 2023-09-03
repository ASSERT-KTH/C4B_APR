n,m,a = map(int, input().split())
s = n / a
q = m / a

if s % 1 > 0:
    s = int(s + 1)
if q % 1 > 0:
    q = int(q + 1)
print(s * q)