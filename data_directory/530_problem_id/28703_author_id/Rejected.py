liste = input().split(" ")

n = int(liste[0])
a = int(liste[1])
b = int(liste[2])
p = int(liste[3])
q = int(liste[4])

m = max(p,q)
res = 0
multa = a
multb = b

# for i in range (1,n+1) :
#     auxa = False
#     auxb = False
#     if i == multa :
#         auxa = True
#         multa += a
#     if i == multb :
#         auxb = True
#         multb += b
#     if auxa and auxb :
#         res += m
#     else :
#         if auxa :
#             res += p
#         elif auxb :
#             res += q
#     #print(i,res)
#             
# print(res)

diva = n//a
divb = n//b
divab = n //(a*b)

if m == p :
    print(diva*p + (divb-divab)*q)
else :
    print(divb*q + (diva-divab)*p)