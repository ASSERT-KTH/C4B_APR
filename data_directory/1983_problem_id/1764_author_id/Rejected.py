#problem number 268B
input=int(input())
sum=0
temp=0
for i in range (input,0,-1):
    sum+=i
    #print(sum)
for i in range(input,0,-1):
    sum+=(i-1)*temp
    temp+=1
if input==2:
    print(2)
else:
    print(sum)