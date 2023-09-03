a, b, c = map(int, input().split())
print(min(2*min((a + b, b + c, c + a)), a+b+c))