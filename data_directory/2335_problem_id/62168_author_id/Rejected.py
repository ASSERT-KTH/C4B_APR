s=input()
k=0
#t=False
#for i in range(len(s)):
 #   if s[i]=='l':
  #      k+=1
   # if not t:
    #    t= not s[i] in 'helo'
h=s.find('h')
e=s.find('e')
o=s.rfind('o')
if h!=-1 and e!=-1 and o!=-1 and h<e<o:
    c=s[e+1:o]
    for i in range(len(c)):
        if c[i]=='l':
            k+=1
            if k==2:
                break
    if k==2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')