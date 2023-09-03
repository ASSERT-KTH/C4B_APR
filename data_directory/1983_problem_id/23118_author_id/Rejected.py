k = int(input())

r = 0

for i in range(k-1):
    r += (k - i)*(i + 1)
    if i > 0:
        r -= 1
print(r+1)