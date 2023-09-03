num = input()

nums = ['4','44','444','7','77','777','47',
        '74','474','447','744','774','747','477']
if num in nums:
    print('YES')

elif num not in nums:
    for i in nums:
        if int(num) % int(i) == 0:
            print('YES')
            break
        else:
            print('NO')
            break
else:
    print('NO')