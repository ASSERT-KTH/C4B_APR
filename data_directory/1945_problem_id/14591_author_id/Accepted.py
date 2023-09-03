a , b , n = map(int,input().split())
flag = False
a = a*10
for i in range(0,10):
    if (a+i)%b == 0:
        a = a + i
        flag = True
        break
if flag == True:
    print(a*(10**(n-1)))
else:
    print("-1")