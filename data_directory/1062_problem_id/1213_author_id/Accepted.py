A = input()

c = 0

count = 0
for i in A:

    if i =='4' or i == '7':
        count = count + 1 

b = str(count)
for i in b:
    if i != '4' and i != '7':
        c = 1
        break

if c == 0 :
    print('YES')
else:
    print('NO')