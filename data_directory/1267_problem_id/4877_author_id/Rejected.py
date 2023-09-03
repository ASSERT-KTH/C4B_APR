input()
s = input()
for c in s:
    if c != '4' and c != '7':
        print('NO')
        break
else:
    if s[:len(s) // 2] == s[-1:len(s)//2-1:-1]:
        print('YES')
    else:
        print('NO')