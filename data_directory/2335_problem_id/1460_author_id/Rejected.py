n=input()
hi=n.find("h")
ei=n.find("e")
li=n.find("l")
lli=n.find("l",n.find("l")+1)
oi=n.find("o")
if hi!=-1 and ei!=-1 and li!=-1 and lli!=-1 and oi!=-1:
    if hi<ei and ei<li and li<lli and lli<oi:
        print("YES")
        exit(0)
print("NO")