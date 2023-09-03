#list(map(int,input().split()))
n,k = map(int,input().split())
totale = 4*60
cont = 0
i = 0
totale -= k
while(True):
   i += 1
   if((totale - (i*5))>=0 and n>0) : 
      n -= 1
      
      totale = (totale - (i*5))
      cont += 1

   else:
      break
print(cont)