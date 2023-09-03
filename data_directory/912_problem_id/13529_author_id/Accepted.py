a,b=map(int,input().split())
b=(240-b)//5
i=0
while (i<a)and(b>=0):
    i+=1
    b-=i
print(i-(b<0))