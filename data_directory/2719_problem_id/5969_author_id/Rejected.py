x, y = list(map(int, input().split()))
years = 0
while x <= y:
    x *= 3
    y *= 2
    if x > y:
        break
    years += 1
print(years)