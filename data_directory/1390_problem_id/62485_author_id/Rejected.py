import math

data = input().split()

N, X, Y = int(data[0]), int(data[1]), int(data[2])

print(math.ceil(N * (Y/100)) - X)