from sys import stdin,stdout
inp=stdin.readline().strip("\n")
if(inp.isupper()):
    print(inp.swapcase())
elif(inp[0].islower() and inp[1:].isupper()):
     print(inp.swapcase())
elif(inp[0].islower() and len(inp)==1):
     print(inp.swapcase())
else:
    print(inp)