p=int(input())
o=input()
while "RR" in o:
    o=o.replace("RR", "R")
while "GG" in o:
    o=o.replace("GG", "G")
while "BB" in o:
    o=o.replace("BB", "B")
print(p-len(o))
print(o)