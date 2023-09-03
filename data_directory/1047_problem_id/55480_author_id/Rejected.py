n = input()
if n[1] > '5':
    if n[0] == '1': n = '20'
    else: n = '10'
elif n[3:] >= n[1] + n[0]:
    n = str((int(n[:2]) + 1) % 24)
    if len(n) == 1: n = '0' + n
print(n[0] + n[1] + ':' + n[1] + n[0])