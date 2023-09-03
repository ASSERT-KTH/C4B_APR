num = int(input())
stones = list(input())
l = []
first = stones[0]
n = 0
for i in range(1,len(stones)):
    if first == stones[i]:
        l.append(stones[i])
    else:
        first = stones[i]
print(len(l))