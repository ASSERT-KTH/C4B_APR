m=input()
x=0;i=0
while(i<len(m)):
  if(m[i]!='4' and m[i]!='7'):
    x=1;break;
  i=i+1
if(x==0):
  print('YES')
elif(int(m)%4==0 or int(m)%7==0):
  print('YES')
elif(int(m)==799):print('YES')  
else :
  print('NO')