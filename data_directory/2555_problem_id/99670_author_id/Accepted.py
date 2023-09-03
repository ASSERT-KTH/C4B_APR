p = input()
p.split()
y = [int(i) for i in p]
m = y[0]
count = 1
a = len(y)
x=-1
for i in range(1,a):
  if y[i]==m:
    count = count+1
    if count==7:
        x=0
        break
  else:
    m = y[i]
    count = 1

if x==0:
  print('YES')
else:
  print('NO')