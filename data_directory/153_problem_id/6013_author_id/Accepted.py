x=int(input())
if(x%2==0 and x>=6):
  if((x%2)%2==1):
    print(x//4)
  else: print((x-1)//4)  
else:print("0")