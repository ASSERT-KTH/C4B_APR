def gcd(a,b):
  while b:
    a,b = b,a%b
  return a

a,b,c = map(int,input().split())
g = gcd(a,b)
if c%g != 0:
  print('No')
else:
  a //= g
  b //= g
  c //= g
  for i in range(c//a+1):
    done = False
    for j in range(c//b+1):
      v = a*i+b*j
      if v == c:
        print('Yes')
        done = True
        break
      elif v > c:
        break
    if done:
      break
  else:
    print('No')