#811A
x,y=input().split()
Vladik=int(x)
Valera=int(y)
i=1
while True :
  Vladik=Vladik-i
  if(Vladik<0):
    print("Vladik")
    break
  i=i+1
  Valera=Valera-i  
  if(Valera<0):
    print("Valera")
    break
  i=i+1