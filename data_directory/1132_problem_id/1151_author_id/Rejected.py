n=int(input())
c=0
if n%4==0 or n%7==0:
    c=1
    print('YES')
n=str(n)
if c==0:
    if n.count('4')+n.count('7')==len(n):
        print('YES')
    else:
        print('NO')