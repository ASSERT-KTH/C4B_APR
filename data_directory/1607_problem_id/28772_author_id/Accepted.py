def count(x):
  if x < 10:
    res = x
  else:  
    f = x % 10
    d = x // 10
    co = 1
    res = 9
    while x > 99:
      res += 9*co
      co *= 10
      x //= 10
    x //= 10 
    res += d - co
    if f >= x: 
      res += 1
  return res 

l, r = map(int, input().split())
print(count(r) - count(l-1))