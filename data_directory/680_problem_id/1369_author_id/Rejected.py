n=int(input())
if n<3:
  print ("-1")
elif n*n%4:
  print(int(n*n/2),int(n*n/2+1))
else:
  print(int(n*n/4-1),int(n*n/4+1))