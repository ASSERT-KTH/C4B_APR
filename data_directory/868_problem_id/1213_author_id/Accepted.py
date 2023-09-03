n=int(input())

if n == 0:
    print(1)
elif (n-1)%4 == 0:
    print(8)
elif (n-2)%4 == 0:
    print(4)
elif (n-3)%4 == 0:
    print(2)
elif (n-4)%4 == 0:
    print(6)