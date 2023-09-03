n,m = map(int, input().split())
sum = 0
for i in range(1, n + 1):
    sum = sum +  (m+i%5)//5
print(sum)