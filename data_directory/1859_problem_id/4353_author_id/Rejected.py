s=input()
t=3+(s[0]>'f')
p=s.find('ru',t+1)
print(s[:t]+'://'+s[t:p]+'.ru/'+s[p+2:])