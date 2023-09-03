n = int(input())
#n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
l = 0
for i in range(1,n):
    l += i * (n - i)
print(l + n)