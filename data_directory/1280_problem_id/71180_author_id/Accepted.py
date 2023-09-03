from sys import stdin


def mayorvalor(n):
    aux = n[0]
##    print('aux-1',aux)
    for i in n:
        if aux < i:
            aux = i
##    print('AUX',aux)
    return aux



def mes(n,m):
    cont = 1
    res = sum(m)
##    print(res)
    
    if n is 0:
        return n
    else:
        if res < n:
            return -1
        else:
            var = mayorvalor(m)
            suma = var 
            while suma < n:
                var = mayorvalor(m)
                m.remove(var)
##                print('var',var,'m',m)
                var2 = mayorvalor(m)
                suma =suma + var2 
                cont +=1
    return cont       
            
        
        
        
        
def main():
    n = int(stdin.readline())
    m = list(map(int,stdin.readline().split()))
    cont = 0
    print(mes(n,m))
main()