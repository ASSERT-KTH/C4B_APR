s=input()
l=len(s)
c=0
d=0
i=0
k=s.find('1111111')
l=s.find('0000000')
if k>=1 or l>=1:
    print('YES')
else:
    print('NO')