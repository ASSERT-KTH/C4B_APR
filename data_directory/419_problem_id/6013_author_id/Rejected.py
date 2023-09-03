n,a,b=map(int,input().split(' '))
if (n==1):print(n)
elif(b>0):
  print((a+b)%n)
elif(b<0):
  print(-(a+b)%n)
elif (b==0):print(a)