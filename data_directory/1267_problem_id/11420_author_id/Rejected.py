n=int(input())
m=input()
x=m.count('4')+m.count('7')
if x!=n:print('NO')
else:
    if sum(int(m[:n/2]))==sum(int(m[n/2:])):
        print('YES')
    else: print('NO')