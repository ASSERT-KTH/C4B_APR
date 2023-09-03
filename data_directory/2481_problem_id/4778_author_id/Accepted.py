import math

n = int(input())
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

i = int(math.log(math.ceil(n*1.0/5), 2))
ind = math.ceil((n - (2**i - 1)*5) / 2**i)

print(names[ind-1])