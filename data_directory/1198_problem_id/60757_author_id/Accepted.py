flag = 0
str = input()
a = ['H', 'Q', '9']
for i in str:
    if i in a:
        flag = 1
if flag == 1:
    print("YES")
else:
    print("NO")