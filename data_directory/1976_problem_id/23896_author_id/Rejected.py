num = int(input())
stones = input()
l = []
first = stones[0]
n = 0
for i in range(1,num):
    if first == stones[i]:
        n+=1
    else:
        first=stones[i]
        l.append(n)
        n=0
        
if len(l):
    print(max(l))
else:
    print(n)