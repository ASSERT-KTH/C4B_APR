from math import ceil
a=["Sheldon","Leonard","Penny","Rajesh","Howard"]
n=int(input())
m=n
i=1
while m>0:
    m-=5*i
    i+=1
print(a[ceil((m+5*(i-1))/(i-1))-1])