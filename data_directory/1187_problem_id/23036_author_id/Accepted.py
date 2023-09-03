s=input()
r=s[1:]
if(r.isupper() or s.isupper()):
    print(s.swapcase())
elif(len(s)==1):
    print(s.swapcase())
else:
    print(s)