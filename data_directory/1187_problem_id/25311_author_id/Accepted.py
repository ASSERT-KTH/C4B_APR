w = input()

if (w.isupper() is False) and (len(w) is 1):
    w = w.capitalize()
elif (w[1:].isupper() is True) and (w[0].isupper() is False):
    w = w.capitalize()
elif w.isupper() is True:
    w = w.lower()

print(w)