s = input()
m = max(s)
n = sum(map(lambda x: x==m, s))
print(m*n)