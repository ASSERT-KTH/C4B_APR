l=list(input().split())
table={0:52,1:52,2:52,3:52,4:52,5:53,6:53}
if(l[2]=="week"):
    print(table[int(l[0])%7])
else:
    n=int(l[0])
    if(n<=29):
        print(12)
    elif(n>30):
        print(7)
    else:
        print(11)