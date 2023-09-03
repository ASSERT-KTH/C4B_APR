n=int(input())
a = n%10
if a == 0:
    print(1)
elif a == 1 or a == 5 or a == 9:
    print(8)
elif a == 2 or a == 6:
    print(4)
elif a == 3 or a == 7:
    print(2)
elif a == 4or a == 8:
    print(6)