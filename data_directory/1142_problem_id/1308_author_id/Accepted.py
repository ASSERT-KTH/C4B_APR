#   list(map(int,input().split()))
cont = 0
n,a,b = map(int,input().split())
if(a == 0 and b == 0):
   print(1)
else:
      
   for i in range(n):
      if(i-1<= b and n-i>=a):
         cont += 1
   print(cont-1)