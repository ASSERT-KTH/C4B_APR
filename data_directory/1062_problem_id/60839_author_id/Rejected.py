num = list(input())
lucky = 0
for i in range(len(num)):
    if num[i] == '4' or num[i] == '7':
        lucky += 1
if (lucky % 4 == 0 or lucky % 7 == 0) and lucky != 0:
    print('YES')
else:
    print('NO')