x = input()
def f(v):
    if v.isupper():
        return v.lower()
    return v.upper()
if len(x) < 2or  x[1:].isupper():
    x = f(x[0]) + x[1:].lower()
    
print(x)