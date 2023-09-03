c, v0, v1, a, l = map(int, input().split())

s = v0
i = 1
while (c > s):
    s+=min(v0 + i * a, v1)
    i+=1
    s-=l

print(i)