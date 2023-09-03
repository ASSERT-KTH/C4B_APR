s=input()
h=int(s[:2])

m=int(s[3:])

mm=int(s[1]+s[0])


if m<mm:
    print(s[0]+s[1]+':'+str(mm))
else:
    h=(h+1)%24;
    
    if(h<10):
        h='0'+str(h)
        print(h+':'+h[1]+h[0])
    else:
        t=str(h)
        print(t+':'+t[1]+t[0])