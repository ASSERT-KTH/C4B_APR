#   list(map(int,input().split()))
cont = 0
n,a,b = map(int,input().split())
for i in range(n):
   if(i-1<= b and n-i>=a):
      cont += 1
print(cont-1)