n, m = map(int, input().split())
if n>m:
  a=n-m
else:
  a=m-n
if a>1:
  print("NO")
elif a==0 and (m==0 or n==0):
  print("NO")
else:
  print("YES")