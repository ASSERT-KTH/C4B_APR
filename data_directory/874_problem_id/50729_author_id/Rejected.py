s=input()

n=int(s[0])
k=int(s[2])


secuencia="1"

i=1
while i<n:
    nueva_secuencia=secuencia[:]+str(i+1)+secuencia[:]
    secuencia=nueva_secuencia
    i+=1


print(secuencia[k-1])