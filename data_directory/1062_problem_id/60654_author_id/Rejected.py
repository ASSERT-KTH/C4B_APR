a=int(input())
a=list(str(a))
T="YES"

for x in a:
    if (x!="4" and x!="7"):
        T="NO"

H=len(a)

H=list(str(H))

if (T == "YES"):
    for x in H:
        if (x!="4" and x!="7"):
            T="NO"


print(T)