input()
s = input()
for c in s:
    if c != '4' and c != '7':
        print('NO')
        break
else:
    if (sum([int(i) for i in s[:len(s) // 2]]) ==
        sum([int(i) for i in s[-1:len(s)//2-1:-1]])):
        print('YES')
    else:
        print('NO')