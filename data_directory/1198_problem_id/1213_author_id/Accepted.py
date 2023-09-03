A = input()
a = 0
for i in A :
    if i == 'H' or i == 'Q' or i == '9' :
        print('YES')
        a = 1
        break
if a == 0:
    print('NO')