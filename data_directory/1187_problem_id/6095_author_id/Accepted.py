x=input()
if x.isupper() or (x[0].islower() and x[1:len(x)].isupper()) or (len(x)==1 and x.islower()):
    x=x.swapcase()
print(x)