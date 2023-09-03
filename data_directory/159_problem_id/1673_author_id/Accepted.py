n = input().split()
if n[-1] == 'month':
    if n[0] == '31':
        print(7)
    elif n[0] == '30':
        print(11)
    else:
        print(12)
else:
    if n[0] in ['1','2','3','4','7']:
        print(52)
    else:
        print(53)