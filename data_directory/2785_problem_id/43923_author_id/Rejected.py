s=input()
n=len(s)
z=''
#print(s,' ',z)
k=0
mm=0
vk='VK'
vv='VV'
kk='KK'
while vk in s:
    m=s.index(vk)
    #print(m)
    z=s[:m]
    s=s[m+2:]
    k+=1
    if (vv in z) or (kk in z):
        mm=1
    #print(s)
    #print(z)
if k==0:
    z=s
#print(mm)

if (vv in z) or (kk in z):
    mm=1
print(k+mm)