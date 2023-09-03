Location=str(input())
i=0
k=1
for i in range(len(Location)-1):
     if Location[i]==Location[i+1]:
          k+=1
     elif k<7:
          k=1
     else:
          print('YES')
          break

if k<7:
     print('NO')