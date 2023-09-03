l=input().split()
x=int(l[0])
y=int(l[1])
s=int(l[2])
def gcd(a, b):
 if a < b:
  a, b = b, a

 while b != 0:
  temp = a % b
  a = b
  b = temp

 return a
while s>0:
    n=gcd(x,s)
    s=s-n
    if s==0:
        print(0)
        quit()
    m=gcd(y,s)
    s=s-m
    if s==0:
        print(1)
        quit()