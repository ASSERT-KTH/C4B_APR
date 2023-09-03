s=input()
k=0
#t=False
#for i in range(len(s)):
 #   if s[i]=='l':
  #      k+=1
   # if not t:
    #    t= not s[i] in 'helo'
h=s.find('h')
o=s.rfind('o')
if h!=-1 and 0!=-1:
    c=s[h+1:o]
    e=c.find('e')
    if e!=-1:
        g=c[e+1:len(s)]
        for i in range(len(g)):
            if g[i]=='l':
                k+=1
                if k==2:
                    break
        if k==2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')