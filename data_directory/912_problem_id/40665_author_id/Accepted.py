n, k = (int(x) for x in input().split())
time = 240 - k
r = 0
while time >= 0 and r <= n:
    r += 1
    time -= 5*r
print(r-1)