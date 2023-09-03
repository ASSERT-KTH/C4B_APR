n=int(input())
def S(x):
  if x>n:return 0
  return 1+S(x*10)+S(x*10+1)
print(S(1))