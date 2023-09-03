l=[]
for x in range(0,26):
    l.append(0)

a=input()
a=list(a)

for x in a:
    l[ord(x.lower())-97]=1

t=0
for x in l:
    t=t+x

if t%2==0:
    print("Charlar con ella!")

else:
    print("¡IGNORALO!")