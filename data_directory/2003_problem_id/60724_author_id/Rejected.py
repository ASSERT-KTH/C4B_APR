a = input()
b= []

if (1000<=int(a)<=9000):
  for k in range(int(a)+1,9001):
    k= str(k)
    for i in k:
        b.append(i)
    c = set(b)

    g = len(c)
    if len(a)== g:
        print(k)
        break

    b= []