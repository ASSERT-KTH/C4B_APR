c, v0, v1, a, l = map(int, input().split())

i = 1
while (c > v0):
    v0+=min(v0 + i * a, v1)
    i+=1
    v0-=1

print(i)