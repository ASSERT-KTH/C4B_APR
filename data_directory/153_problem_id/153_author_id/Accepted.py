n = int(input())
#n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
if n % 2 == 0:
    print(n // 4 - (n % 4 == 0))
else:
    print(0)