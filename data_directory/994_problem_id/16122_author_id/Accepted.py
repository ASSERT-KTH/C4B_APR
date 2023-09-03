from math import ceil
q = input().split(" ")
a = int(q[2])
n = int(q[0])
m = int(q[1])
answer = ceil (m/a) * ceil (n/a)
print(answer)