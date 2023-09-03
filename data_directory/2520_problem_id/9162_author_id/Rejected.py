l = input().split()
n=0
for i in range(len(l)):
    l[i] = int(l[i])
    if (l[i])>n:
        n=(l[i])
a=(6-n)+1
if a==1:
    print('1/6')
if a==2:
    print('1/3')
if a==3:
    print('1/2')
if a==4:
    print('2/3')
if a==5:
    print('5/6')
if a==6:
    print(1)