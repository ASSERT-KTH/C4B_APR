hq=['H','Q','9']
a=[str(i) for i in (' '.join(input())).split()]
f=False
for i in a:
    if i in hq:
        f=True
        break
print('YES' if f else 'NO')