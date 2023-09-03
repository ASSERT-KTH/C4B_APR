n = int(input())
#n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
m = n // 7
l = n - m * 7
print(m * 2 + (l == 6), m * 2 + (l > 0) + (l > 1))