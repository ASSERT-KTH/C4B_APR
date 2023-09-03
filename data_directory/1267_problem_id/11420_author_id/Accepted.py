n=int(input())
m=input()
x=m.count('4')+m.count('7')
if x!=n:print('NO')
else:
    if m[:n//2].count('4')==m[n//2:].count('4'):
        print('YES')
    else: print('NO')