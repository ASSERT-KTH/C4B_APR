num = input()

g = 0
nums = ['4','44','444','7','77','777','47',
        '74','474','447','744','774','747','477']
if num in nums:
    print('YES')

elif num not in nums:
    for i in nums:
        if int(num) % int(i) == 0:
            print('YES')
            g += 1
            break
    if g == 0:
        print('NO')
else:
    print('NO')