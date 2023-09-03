k = int(input())

a = list(map(int,input().split()))

sort = sorted(a,key=int, reverse=True)

result = 0
count = 0

for value in sort:
    if result >= k:
        break
    result += value
    count += 1
    
print(count)