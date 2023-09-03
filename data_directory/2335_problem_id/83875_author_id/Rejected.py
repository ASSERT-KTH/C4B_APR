n = int(input())
lt = []
scr = 0

for i in range (0,n):
    check = 0
    m = input()
    temp = m.split()
    for i in temp :
        if i == '1':
            check+=1
    if check >=2:
        scr+=1
print(scr)