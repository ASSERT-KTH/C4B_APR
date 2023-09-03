from sys import stdin
def quickSort(lst):
    if len(lst) <= 1: 
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quickSort(larger) + [lst[0]] + quickSort(smaller)
def main():
    x=int(stdin.readline().strip())
    lst=list(map(int,stdin.readline().strip().split()))
    orden=(quickSort(lst))
    suma=orden[0]
    cont=1
    for i in range(len(orden)-1):
        if suma<x:
            suma+=orden[i+1]
            cont+=1
    if x==0:
        print(0)
    elif suma < x:
        print(-1)
    else:
        print(suma)

        
        
    

main()