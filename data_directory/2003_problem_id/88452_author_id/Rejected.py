# Programa para saber de ese anio que año tiene todos los digitos diferentes

# Modulo para verificar si ese año es diferente
def DigitosDiferentes(Anio):
    A = Anio//1000
    B = (Anio%1000)//100
    C = (Anio%100)//10
    D = Anio%10
    L = []
    L.append(A)
    L.append(B)
    L.append(C)
    L.append(D)
    L.sort()
    return((int(L[0]))!=(int(L[1]))!=(int(L[2]))!=(int(L[3])))
# Modulo para devolver el año mayor al año entregado con diferentes digitos
def SiguienteAnioDiferente(Anio):
    for k in range(Anio+1,9001):
        if(DigitosDiferentes(k)):
            break
    return k

# Programa Principal
Anio = input()
A = int(Anio)
print(SiguienteAnioDiferente(A))