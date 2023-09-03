a=int(input())

i=0

while 5*(2**i-1)<a:

    i+=1


sheldon=[]

for x in range(5*(2**(i)-1)-5*2**(i-1)+1,5*(2**(i)-1)-4*2**(i-1)+1):
  
  sheldon.append(x)



leonard=[]

for x in range(5*(2**(i)-1)-4*2**(i-1)+1,5*(2**(i)-1)-3*2**(i-1)+1):
  
  leonard.append(x)



penny=[]

for x in range(5*(2**(i)-1)-3*2**(i-1)+1,5*(2**(i)-1)-2*2**(i-1)+1):
  
  penny.append(x)



rajesh=[]

for x in range(5*(2**(i)-1)-2*2**(i-1)+1,5*(2**(i)-1)-2**(i-1)+1):
  
  rajesh.append(x)



howard=[]

for x in range(5*(2**(i)-1)-2**(i-1)+1,5*(2**(i)-1)+1):
  
  howard.append(x)



if a in sheldon:

    print("Sheldon")



elif a in leonard:
  
  print("Leonard")



elif a in penny:
  
  print("Penny")



elif a in rajesh:
  
  print("Rajesh")



elif a in howard:
  
  print("Howard")