s=input()
ss=''
sss='qwertyuiopasdfghjklzxcvbnm'
ssss='QWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(len(s)):
    if s[i] in 'AEIOUaeiou':
        pass
    else :
        if s[i] in ssss :
               ss=ss+sss[ssss.find(s[i])]
        else :
               ss=ss+s[i]
k='.'
print('.'+k.join(list(ss)))