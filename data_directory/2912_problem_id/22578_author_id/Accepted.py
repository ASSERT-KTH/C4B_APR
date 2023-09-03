def fact(x):
      r=1
      for i in range(2,x+1):
            r=r*i
      return r
ch=input("")
l=ch.split(" ")
a=int(l[0]);b=int(l[1])
print(fact(min(a,b)))