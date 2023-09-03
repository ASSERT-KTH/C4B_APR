s=list(input())
L=['Q','H','9','+']
q=0
for i in s:
    if(i in L):
        print('YES')
        q=1
        break
if(q==0):print('NO')