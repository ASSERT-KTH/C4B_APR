a=input()
b=list(a)
characters = ('H','Q','9')
j=0
while j<len(b):
  if b[j] in characters:
    print("YES")
    break
  else:
    j+=1
else:
  print("NO")