k, r = map(int, input())
print(min(i for i in range(1,11) if k * i % 10 == r or k * i % 10 == 0))