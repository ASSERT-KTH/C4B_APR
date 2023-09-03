a=['Sheldon','Leonard','Penny','Rajesh','Howard']
n= int(input())-1
i= 5
while n>=i:
    n-=i
    i*= 2
p=int(n/(i/5))
print (a[p])