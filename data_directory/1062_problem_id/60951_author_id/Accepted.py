n = list(input())
count = 0
for itch in n:
    if itch == '4' or itch == '7':
        count += 1
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')