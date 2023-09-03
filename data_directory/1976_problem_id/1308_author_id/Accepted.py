#list(map(int,input().split()))
times  = int(input())
ane = list(input())
count = 0
for i in range(len(ane)-1):
   if(ane[i] == ane[i+1]):
      count = count + 1
print(count)