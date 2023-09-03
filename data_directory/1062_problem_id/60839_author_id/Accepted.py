num = list(input())
lucky = 0
for i in range(len(num)):
    if num[i] == '4' or num[i] == '7':
        lucky += 1
if (lucky in {4,7,44,47,74,77,444,447,474,477,744,747,774,777}) and lucky != 0:
    print('YES')
else:
    print('NO')