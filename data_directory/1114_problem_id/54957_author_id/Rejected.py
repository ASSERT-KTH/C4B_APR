a=input()
b=input()
c=input()
if a[0]==c[2]:
    d=0
else:
    d=1
if a[1]==c[1]:
    d=0
else:
    d=1
if a[2]==c[0]:
    d=0
else:
    d=1
if b[0]==b[2]:
    d=0
else:
    d=1
if d==0:
    print('YES')
if d==1:
    print('NO')