a, b = list(map(int, input().split()))
c = max(a, b)
ans = 0
for i in range(c):
  for j in range(c):
    if(i**2+j == a and i+j**2 == b):
      ans+=1
      
print(ans)