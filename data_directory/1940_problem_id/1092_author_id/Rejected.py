def Primo(N):
    div = 0
    if N>1:
        for k in range (2,N):
            if N%k==0:
                div +=1
        if div ==0:
            return True
        else:
            return False
    else:
        return False

def CasiPrimo(N):
    Div = []
    for k in range (2,N):
            if N%k==0:
                Div.append(k)
    Cont = 0
    for k in range (len(Div)):
        if Primo(Div[k]):
            Cont +=1
    if Cont==2:
        return True
    else:
        return False
C = 0
N = int(input())
for k in range (N+1):
    if CasiPrimo(k):
        C += 1
print(C)