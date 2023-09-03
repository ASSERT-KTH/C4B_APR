string=(input())
t=0
if(len(string)<7):
    print('NO')
else:
    for x in range(len(string)-6):
        if (string[x:x+7]=='1111111' or string[x:x+7]=='0000000'):
            t+=1
            print('YES')
            break
    if(t==0):
        print('NO')