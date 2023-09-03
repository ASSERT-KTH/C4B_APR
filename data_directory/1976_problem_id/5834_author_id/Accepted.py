a = int(input())
stones = input()
counter = 0
result = 0

for i in stones:
    if counter < a - 1 and stones[counter + 1] is i:
        result += 1
    counter += 1
print(result)