x= int(input())
y= int(input())
k=False
u=0
for i in range (1,32) :
    if y==x**i :
        k=True
        u=i
        break

if k==False :
    print ("NO")
else :
    print ("YES")
    print ('1')