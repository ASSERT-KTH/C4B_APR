d1, d2, d3 = map(lambda x: int(x), input().split(' '))

path = 0
path += min(d1, d2)
path += min(d1 + d2, d3)
path += max(d1, d2)

print(path)