x = input()
if(x.isupper() or x[1:].isupper()):
    x = x.lower()
print(x)