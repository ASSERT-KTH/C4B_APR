def fact(x):
      r=1
      for i in range(2,x+1):
            r=r*i
      return r
def ex():
      ch=input("")
      l=ch.split(" ")
      a=int(l[0]);b=int(l[1])
      m=max(a,b)
      n=min(a,b)
      c=fact(m)
      d=fact(n)
      if c%d==0 :
            return d
      else :
            for i in range(d//2,0,-1):
                  if (d%i==0) :
                        if c%i==0 :
                              return i
print(ex())