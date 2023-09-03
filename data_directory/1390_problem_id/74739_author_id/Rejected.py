import math

n, k, p = map(int, input().split())

need = math.ceil(n*p/100)

print(need-k)