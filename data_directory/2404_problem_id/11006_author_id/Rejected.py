l1=input()
l2=input()
l3=input()
l4=input()
l5=input()
l6=input()
l7=input()
l8=input()
c=0
if(l1.count('B')==8 ):
  c+=1
else:
  c+=l1.count('B')
if(l2.count('B')==8):
  c+=1
else:
  c+=l2.count('B')  
if(l3.count('B')==8):
  c+=1
else:
  c+=l3.count('B')  
if(l4.count('B')==8 ):
  c+=1
else:
  c+=l4.count('B')
  
if(l5.count('B')==8 ):
  
  c+=1
else:
  c+=l5.count('B')
  
if(l6.count('B')==8):
  c+=1
else:
  c+=l7.count('B')  
if(l7.count('B')==8 ):
  c+=1
else:
  c+=l7.count('B')  
if(l8.count('B')==8 ):
  c+=1
else:
  c+=l8.count('B')  

print(c)