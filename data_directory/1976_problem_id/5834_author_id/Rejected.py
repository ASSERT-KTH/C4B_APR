a = int(input())
stones = input()
counter = 0
result = 0

for i in stones:
    if stones[i + 1] == i:
        result += 1
        
print(result)