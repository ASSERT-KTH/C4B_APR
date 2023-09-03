import sys

def Btrip(num,lista):
    cont = 1
    suma = sum(lista)
    print('sum',suma)
    
    if num is 0:
        return num
    else:
        if suma < num:
            return '-1'
        else:
            
            maxi = max(lista)
            print('maxi',maxi)
            while maxi < num:
                a = max(lista)
                print('a',a)
                lista.remove(a)
                print('list',lista)
                b = max(lista)
                print('b',b)
                maxi =maxi + b
                print('maxi2',maxi)
                cont +=1
        print(lista)
        return cont
    
def main():
    num = int(sys.stdin.readline())
    listameses = list(map(int,sys.stdin.readline().split()))
    print(Btrip(num,listameses))
main()