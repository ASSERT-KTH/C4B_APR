m, d = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if d <= 5 +(31 - days[m-1]):
    print(5)
else:
    print(6)