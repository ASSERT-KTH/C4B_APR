n=input()
ans=2**(len(n)-1)
n1=''
for i in range(1,len(n)):
    if int(n[i])>0:n1+='1'
    else:n1+='0'
n1=0b0+int(n1)
print(ans+n1)