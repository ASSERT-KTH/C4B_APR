s=input()
h=int(s[:2])

m=int(s[3:])

mm=int(s[1]+s[0])
if h==6 or h==7:
    print("10"+':'+"01")
elif h==8 or h==9:
    print("10"+':'+"01")
elif h==16 or h==17:
    print("20:02")
elif h==18 or h==19:
    print("20:02")
elif h==5 and m>49:
    print("10:01")
elif h==15 and m>50:
    print("20:02")
else:
    
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