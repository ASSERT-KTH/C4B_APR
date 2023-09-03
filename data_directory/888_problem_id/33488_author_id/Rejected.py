a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

ans = 0
count = 1000

while(count>=0):
  x = count/4
  y = count/2
  z = count
  if(a>=x and b>=y and c>=z):
    ans = x+y+z
    break
  count-=4
ans = int(ans)
print(ans)