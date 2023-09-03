a=int(input())
if (str(a).replace("4",'')).replace("7","")=="":
    print("YES")
else:
    m="0"
    d=-1
    h=True
    while int(m)<=(a**0.5) :
        d+=1
        m=bin(d)[2:]
        m=(m.replace("0","4")).replace("1","7")
        if a%int(m)==0 :
            print("YES")
            h=False
            break
    if h : print("NO")