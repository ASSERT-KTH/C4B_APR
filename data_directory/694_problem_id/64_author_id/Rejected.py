x=input()
if x=="a1" or x=="a8" or x=="h1" or x=="h8":
    print(3)
elif x.count("a")==1 or x.count("h")==1 and x.count("1" or "8")==0:
    print(5)
elif x.count("1")==1 or x.count("8")==1 and x.count("a")==0 and x.count("h"):
    print(5)
else:
    print(8)