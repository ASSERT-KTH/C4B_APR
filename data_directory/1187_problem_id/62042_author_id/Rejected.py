C = input()
C = list(C)
def VerCasos(C):
    if C[0].islower() == True:
        k = 1
        while k < len(C):
            if (C[k].isupper()) == True:
                caso = 0
                k +=1
            else:
                caso = 1
                break
    else:
        if C[0].isupper() == True:
            k = 1
            while k < len(C):
                if (C[k].isupper()) == True:
                    caso = 2
                    k +=1
                else:
                    caso = 1
                    break
    return caso            
            
if VerCasos(C) == 0:
    C = "".join(C)
    C = C.lower()
    C = list(C)
    C[0] = C[0].upper()
    C = "".join(C)
if VerCasos(C) == 1:
    C = "".join(C)
if VerCasos(C) == 2:
    C = "".join(C)
    C = C.lower()
print (C)