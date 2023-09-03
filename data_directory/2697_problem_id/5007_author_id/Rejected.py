def gcd(a,b):
  while b:
    a,b = b,a%b
  return a

a,b = map(int,input().split())
c,d = map(int,input().split())
A = d//a
D = d%a
C = b//c
B = b%c
g = gcd(a,c)
aa = a//g
cc = c//g
delta = D-B
if delta%g != 0:
  print(-1)
else:
  delta //= g
  for x in range(-A,-A+cc):
    done = False
    for y in range(-C,-C+aa):
      if aa*x-cc*y == delta:
        print(b+g*aa*(x+A))
        done = True
        break
    if done:
      break
  else:
    print(-1)