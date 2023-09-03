x=int(input())
mi=2*int((x/7))
ma=0
j=x%7
if j==0:
    ma=mi
elif j==1:
    ma=mi+1
else:
    ma=mi+2
print (str(int(mi))+" "+str(int(ma)))