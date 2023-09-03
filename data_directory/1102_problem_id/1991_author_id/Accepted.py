a = (input()).lower()
a = list(a)
c = 0
d = list()
for p in a:
    if p == "a" or p == "e" or p == "i" or p == "o" or p == "u" or p == "y":
        continue
    else:
        d.append(p)
s = ""
for p in d:
    s = s + "." + p

print(s)