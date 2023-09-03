def READ():
    return map(int, input().split())

vladikTurn = True
valeraTurn = False

vladik = True
valera = True

a, b = READ()

for f in range(1, 10**9+1, 1):
    if vladikTurn :
        a -= f
        
        if a<0:
            ptint("Vladik")
            exit(0)
        
        vladikTurn = False
        valeraTurn = True
    
    elif valeraTurn:
        b -= f
        
        if b<0:
            print("Valera")
            exit(0)
        
        valeraTurn = False
        vladikTurn = True

#if vladik:
#    print("Valera")
#
#else:
#    print("Vladik")