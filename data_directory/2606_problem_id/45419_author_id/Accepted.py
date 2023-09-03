q,w=[int(x) for x in input().split()]
e=""
#for i in range(q):
#    if i<w:
#        e += chr(ord('a')+i)
#    else:
#        e += 'a'
#print(e)
i=0
pis=0
while (pis < q):
    e += chr(ord('a')+i)
    i = i + 1
    pis = pis + 1
    if(i>=w):
        i=0
print(e)