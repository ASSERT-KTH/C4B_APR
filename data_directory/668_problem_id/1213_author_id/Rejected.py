n = int(input())
s = ''
for i in range(0,n):
    if i %2 == 0:
        if i != n-1:
            s = s+'I hate that'+' '
        else:
            s = s+'I hate it'
    else:
        if i != n -1:
            s = s+'I love that'+' '
        else:
            s = s+'I hate it'
print(s)