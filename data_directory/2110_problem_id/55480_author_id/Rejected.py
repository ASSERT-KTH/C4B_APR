t, p = input().lower(), 'abcdefghijklmnopqrstuvwxyzA'[int(input())]
print(''.join(i.upper() if i < p else i for i in t))