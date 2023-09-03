a = list(map(int, input().split()))
if a[0] * a[2] * a[4] < a[1] * a[3] * a[5]:
    print('Ron')
else:
    if (0 == a[0] * a[2] * a[4]) ^ (0 == a[1] * a[3] * a[5]):
        print('Hermione')
    elif 0 == a[0] * a[2] * a[4] == a[1] * a[3] * a[5]:
        if a[2] == 0 and a[3] != 0:
            print('Ron')
        else:
            print('Hermione')
    else:
        print('Hermione')