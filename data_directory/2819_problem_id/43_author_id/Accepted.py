nums = input()
nums = nums.split(' ')
nums = list(map(int,nums))
if nums[0] == nums[1]:
    print(nums[0])
elif (nums[1] - nums[0]) % 2 == 0:
    print('2')
elif (nums[1] - nums[0]) % 2 == 1 and (nums[0] % 2 == 0 or nums[1] % 2 == 0):
    print('2')
else:
    print('3')