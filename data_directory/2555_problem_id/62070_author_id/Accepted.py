gamers=input()
pol=1
i=1
for j in range(1,len(gamers)):
    if gamers[j]==gamers[j-1]:
        pol+=1
    elif pol<7 and gamers[j]!=gamers[j-1]:
        pol=1
if pol>=7:
    print('YES')
else:
    print('NO')