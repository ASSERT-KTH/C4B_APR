n = int(input())
#n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
s = ''
for i in range(1, 1000):
    s += str(i)
print(s[n - 1])