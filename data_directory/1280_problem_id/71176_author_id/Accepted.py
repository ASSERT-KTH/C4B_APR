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
    i=len(m)-1
    s=0
    k=0
    while i>=0:
        if s<n:
            s=s+m[i]
            k+=1
        i-=1
    
    if s<n:
        print("-1")
    else:
        print(k)

main()