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
if (var2>=var1):
 print(factorial(var1))
if (var1>var2):
 print(factorial(var2))