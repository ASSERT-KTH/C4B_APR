def valera(my_array, n):
    for i in range(1, n-1):
        for j in range(i, n-1):
            if my_array[j] > my_array[j+1]:
               my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array

n = input()
n = int(n)
if n == 1 or n == 2 :
    print(-1)
else:
    my_array = [i for i in range(n,0,-1)]
    result = valera(my_array, n)
    for el in result:
        print(el, end=' ')