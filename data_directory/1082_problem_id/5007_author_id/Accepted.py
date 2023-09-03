k = int(input())
l = int(input())
r = -1
while l > 1:
  if l%k != 0:
    print('NO')
    break
  else:
    r += 1
    l //= k
else:
  print('YES')
  print(r)