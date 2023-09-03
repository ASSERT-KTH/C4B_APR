a = list(input().split())
b = []
for i in range(len(a)):
    if a[i] not in b:
        b += a[i]
print(4-len(b))