n=input()
hi=n.find("h")
ei=-1
li=-1
lli=-1
oi=-1
if hi!=-1:
    ei=n.find("e",hi+1)
if ei!=-1:
    li=n.find("l",ei+1)
if li !=-1:
    lli=n.find("l",li+1)
if lli !=-1:
    oi=n.find("o",lli+1)
if hi!=-1 and ei!=-1 and li!=-1 and lli!=-1 and oi!=-1:
    if hi<ei<li<lli<oi:
        print("YES")
        exit(0)
print("NO")