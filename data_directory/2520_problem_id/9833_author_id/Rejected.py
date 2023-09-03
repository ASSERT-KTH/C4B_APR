l=[1,2,3,4,5,6]
a,b=input().strip().split(' ')
a,b=(int(a),int(b))
if a==b:
  print("1/1")
elif a==6 or b==6:
  print("0/1")
else:
  c=7-max(a,b)
  if c==1:
    print("1/6")
  elif c==2:
    print("1/3")
  elif c==3:
    print("1/2")
  elif c==4:
    print("2/3")