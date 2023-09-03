a=str(input())
b=list(a)
v=0
s=['Q','H',9]
for c in b :
    for i in s :
        if c==i :
            v+=1
            print('YES')
            break
    if v!=0 :
        break
if v==0 :
    print('NO')