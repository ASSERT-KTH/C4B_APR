n, k = [int(x) for x in input().split()]
cnt = 0
p = 2
V = []
while p<=n:
  if n%p==0:
    n //= p
    cnt += 1
    V.append(p)
    if cnt==k:
      break
  else:
    p += 1
if cnt==k and n>1:
  V[cnt-1] *= n
print(V)
if cnt<k:
  print(-1)
else:
  for i in range(0,cnt):
    print(V[i], end=' ')