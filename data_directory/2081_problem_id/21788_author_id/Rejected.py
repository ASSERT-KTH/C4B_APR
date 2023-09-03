(n, k) = map(int, input().split(' '))

nums = []
for i in range(n):
    nums.append(i + 1)


temp = nums[k-1]
nums[k-1] = nums[k]
nums[k] = temp

print(' '.join(map(str, nums)))