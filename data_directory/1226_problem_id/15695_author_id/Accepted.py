m=int(input())
reg=input().split()
counter=0
sum1=0
i=0
while sum1<m:
 sum1+=int(reg[i%7])
 counter+=1
 i+=1
print((counter-1)%7+1)