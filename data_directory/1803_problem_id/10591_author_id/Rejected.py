n = int(input())
r = range(max(1, n - 20), n+1)
print(max([lcm(lcm(x,y),z) for x in r for y in r for z in r]))