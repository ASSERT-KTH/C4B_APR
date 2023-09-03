from sys import stdin

def partition(lista):
#Sacado de las diapositivas de la clase
    pivote,menores,mayores=lista[0],[],[]
    for x in range(1,len(lista)):
        if lista[x]<pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores,[pivote],mayores

def quicksort(lista):
#Sacado de las diapositivas de la clase
    if len(lista)<2:
        return lista

    menores,medio,mayores=partition(lista)
    return quicksort(menores)+medio+quicksort(mayores)


def main():
    n=int(stdin.readline())
    m= [int(arr_temp) for arr_temp in stdin.readline().strip().split()]
    m=quicksort(m)
    
    
    k=1
    c=0
    for i in range(n-1):
        r=m.count(m[i])
        if r>c:
            c=r
        if m[i]==m[i+1]:
            
            k-=1
        
        k+=1
    print(c,k)

main()