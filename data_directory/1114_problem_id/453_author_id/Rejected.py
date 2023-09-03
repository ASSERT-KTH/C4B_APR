a=input()
b=input()
c=input()
d=a+b+c
if 'X' in d:
    if d==d[::-1]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')