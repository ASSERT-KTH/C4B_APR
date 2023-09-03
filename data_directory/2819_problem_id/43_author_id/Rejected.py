nums = input()
nums = nums.split(' ')
nums = list(map(int,nums))
if (nums[1] - nums[0]) % 2 == 0:
    print('2')
else:
    print('3')