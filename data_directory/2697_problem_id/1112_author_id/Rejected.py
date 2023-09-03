from sys import exit
a,b=map(int,input().split())
c,d=map(int,input().split())
if b==d:
    print(b)
    exit(0)
if ((b%2!=0 and a%2==0)and(d%2==0))or((d%2!=0 and c%2==0)and(b%2==0)):
    print('-1')
    exit(0)
i=1
while True:
   j=((i*a+b)-d)/c
   m=((i*a+b)-d)//c
   if j-float(m)==0.0:
       print((i*a+b))
       break
   i+=1