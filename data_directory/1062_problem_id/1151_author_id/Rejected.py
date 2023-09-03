n=input()
a=n.count('4')+n.count('7')
if (a%4==0 or a%7==0) and a!=0:
    print('YES')
else:
    print('NO')