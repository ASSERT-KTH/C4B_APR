x = int(input())
if x <= 7:
    if x == 1:
        print(0, 1)
    elif x == 6:
        print(1, 2)
    elif x == 7:
        print(2, 2)
    else:
        print(0, 2)
if x > 7:
    if (x % 7) == 0:
        print(int(2*(x/7)), int(2*(x/7)))
    else:
        if (x % 7) == 1:
            print(2*int(x/7), 2*int(x/7)+1)
        else:
            print(2 * int(x / 7), 2 * int(x / 7) + 2)