a, b = map(int, input().split())
sum = 1
for i in range(1, a + 1):
    sum = i * sum
print(sum)