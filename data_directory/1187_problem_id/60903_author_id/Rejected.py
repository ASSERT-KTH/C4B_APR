x = input()
if len(x) < 2 or x[1:].isupper():
    x = x[0].upper() + x[1:].lower()
print(x)