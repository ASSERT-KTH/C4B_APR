a , b , n = map(int,input().split())
flag = False
for i in range(n):
    flag = False
    a = a*10
    if a%b == 0:
        flag = True
        continue
    for j in range(1,10):
        if ((a+j)%b == 0):
            flag = True
            a = a+j
            break
    if flag == False:
        print("-1")
        exit()
print(a)