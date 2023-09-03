n = int(input())
res = 'I '
for i in range(n):
  res += 'love that ' if i % 2 else 'hate that '
print(res[:-5] + 'it')