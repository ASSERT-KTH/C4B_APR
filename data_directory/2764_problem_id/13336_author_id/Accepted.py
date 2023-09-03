n, k = [int(x) for x in input().split()]

# cnt = ilość podzielników, docelowo ma być równe k
cnt = 0

# p = kolejny podzielnik liczby n
p = 2

# V = lista podzielników 
V = []

while p<=n:
  if n%p==0:
    # p jest podzielnikiem
    n //= p
    cnt += 1
    V.append(p)
    if cnt==k:
      # mamy dość podzielników
      break
  else:
    p += 1
    
# jeśli n jest różne od 1 to dokładamy to do ostatniego podzielnika
if cnt==k and n>1:
  V[cnt-1] *= n

if cnt<k:
  # za mało podzielników
  print(-1)
else:
  # jest OK
  for i in range(0,cnt):
    print(V[i], end=' ')