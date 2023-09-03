a=input()
b=list(a)
if len(b)==1:
  if a==a.upper():
    print(a.lower())
  else:
    print(a.upper())
else:
  if a.lower()==a:
    print(a)
  elif a.upper()==a:
    print(a.lower())
  else:
    if b[0].lower()==b[0]:
      c=a[1::]
      if c.upper()==c:
        print(b[0].upper()+c.lower())
      else:
        print(a)
    elif b[0].upper()==b[0]:
      print(a)