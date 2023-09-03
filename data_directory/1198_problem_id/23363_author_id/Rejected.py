string=input()
code='HQ9+'
for i in string:
    if i in code:
        print('YES')
        break
else:
    print('NO')