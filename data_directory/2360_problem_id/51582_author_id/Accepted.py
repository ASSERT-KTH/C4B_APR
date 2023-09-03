venusian_fingers = [int(n) for n in input().split()]
marsian_fingers = [int(n) for n in input().split()]
yes = False
for i in range(0,2):
    if(marsian_fingers[1-i]<=(venusian_fingers[i]+1)*2 and marsian_fingers[i-1]>=(venusian_fingers[i]-1)):
        yes = True
        break
if(yes):
    print('YES')
else:
    print('NO')