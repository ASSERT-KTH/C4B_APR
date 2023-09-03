a,b,c=map(int,input().split(' '))
if(c==0):
  if(a==b):print('YES')
  else:print('NO')
elif(a+b==0):
  if(c%a==0):print('YES')
  else:print('NO')
elif(abs(b-a)%abs(c)==0):
  print('YES')
else:print('NO')