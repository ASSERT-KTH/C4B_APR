a, b, c = list(map(int, input().split()))

nums = []
for i in range(c):
    if a * i == c:
        print('Yes')
        exit()
    elif a * i > c:
        break
    nums.append(a * i)
for i in range(1, c):
    nums = [x + b for x in nums]
    if c in nums:
        print('Yes')
        exit()
print('No')