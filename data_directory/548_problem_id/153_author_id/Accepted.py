#n = int(input())
n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
l = (n // 5) * (m // 5)
for i in range(1, 5):
    l += ((n - i) // 5 + 1) * ((m - 5 + i) // 5 + 1)
print(l)