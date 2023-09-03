m, d = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m==2 and d ==1:
    print(4)
elif d <= 5 +(31 - days[m-1]):
    print(5)
else:
    print(6)