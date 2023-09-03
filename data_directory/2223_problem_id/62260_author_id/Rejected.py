x=int(input('enter:'))
c=0
for i in range(1,x):
    if i%2==0 :
        if (x-i) %2==0 :
            print('YES')
            c+=1
            break


if c==0 :
    print('NO')