a, b = map(int, input().split())
if (a > b):
    a, b = b, a
sum = 1
for i in range(1, a + 1):
    sum *= i
print(sum)