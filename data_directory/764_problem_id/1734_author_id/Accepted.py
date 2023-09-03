coords = list(map(int, input().split()))
coords.sort()
print(coords[2] - coords[0])