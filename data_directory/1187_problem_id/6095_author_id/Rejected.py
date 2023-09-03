x=input()
if x.isupper() or (x[0].islower() and x[1:len(x)].isupper()):
    x=x.swapcase()
print(x)