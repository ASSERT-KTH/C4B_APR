#Problema 151A

lista=[]

a=input()
a=a.split(" ")
lista.append(a)

menor=0
tostadas= int(((int(a[1])*int(a[2]))/int(a[-2]))/int(a[0]))

limas= int((int(a[3])*int(a[4]))/int(a[0]))

sal= int((int(a[5])/int(a[-1]))/int(a[0]))


if tostadas<limas and tostadas <sal:
    menor=tostadas
elif limas<tostadas and limas<sal:
    menor=limas

elif sal<tostadas and sal<limas:
    menor=sal

print(menor)