n = list(input())
count = 0
for itch in n:
    if itch == '4' or itch == '7':
        count += 1
if (count % 4 == 0 or count % 7 == 0) and count != 0:
    print('YES')
else:
    print('NO')