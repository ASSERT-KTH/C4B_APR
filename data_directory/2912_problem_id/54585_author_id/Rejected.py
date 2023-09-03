import sys
sys.setrecursionlimit(399603090)
nmbrs=input()
numbers=nmbrs.split(" ")
var1=int(numbers[0])
var2=int(numbers[1])
alist=[0]
def factorial(x):
 if x==1:
  return 1
 else:
  return x*factorial(x-1)
def gcd(a,b):
  for i in range(13):
   if i>0:
    if (a%i==0 and b%i==0):
     alist.append(i)

  
f1=factorial(var1)
f2=factorial(var2)
gcd(f1,f2)
print(max(alist))