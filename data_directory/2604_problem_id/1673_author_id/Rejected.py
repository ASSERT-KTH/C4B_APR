m = input()
n = str(int(m[0])-1) + '9' * (len(m)-1)
k = sum(list(map(int, m)))
p = sum(list(map(int, n)))
print(int(m) if p <= k else int(n))