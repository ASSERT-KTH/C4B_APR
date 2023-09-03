a,b=map(int,input().split(' '))
c,d=map(int,input().split(' '))
flag = 0
rick = []
morty = []
for i in range(101):
    rick.append(b + i*a)
    morty.append(d + i*c)
for i in range(len(rick)):
    if rick[i] in morty:
        print(rick[i])
        break
    else:
        flag += 1
if flag==len(rick):
    print(-1)