k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
wyn=0
for x in range(1,d+1):
    if x%k==0 or x%l==0 or x%m==0 or x%n==0:
        wyn +=1
    
print(wyn)