p=input()
i=0
while i<len(p):
    if p[i]=='H' or p[i]=='Q' or p[i]=='9':
        print ('YES')
        break
    i+=1
else:
    print ('NO')