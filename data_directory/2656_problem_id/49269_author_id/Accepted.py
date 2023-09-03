N, K = [n for n in input().split()]
K = int(K)

i = 0
dels =0
for d in reversed(N):
  if i < K:
    if d != '0':
      dels += 1
      i -= 1
  else:
    break
  i += 1

l = len(N)
if i + dels == l or K >= l:
  print(len(N)-1)
else:
  print(dels)