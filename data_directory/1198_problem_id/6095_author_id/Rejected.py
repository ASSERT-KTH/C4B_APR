p=input()
i=0
while i<len(p):
    if p[i]=='H' or p[i]=='Q' or p[i]=='9' or p[i]=='+':
        print ('YES')
        break
    i+=1
else:
    print ('NO')