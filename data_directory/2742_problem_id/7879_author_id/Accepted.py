n = int(input())
if (n%2) :
  n = (n-3)
  print('7', end="")
  while n > 0 :
    print('1', end="")
    n-=2
else :
  while n > 0:
    print('1', end="")
    n-=2