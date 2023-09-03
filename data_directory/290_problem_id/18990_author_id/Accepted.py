a, b, c = list(map(int, input().split()))

nums = []
for i in range(c + 1):
    if a * i == c:
        print('Yes')
        exit()
    elif a * i > c:
        break
    nums.append(a * i)
for i in range(1, c + 1):
    nums = [x + b for x in nums]
    if c in nums:
        print('Yes')
        exit()
print('No')