nums = []

for i in range(0,4):
    nums.append((int(input())))


d = int(input())

l = len(nums)

result = 0
for i in range(0, d):
    for item in nums:
        if i/item == int(i/item) and item <= i:
            result+=1
            break
        

print(result)