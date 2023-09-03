s = input()
x = []
for i in s:
    if i == 'h' or 'e' or 'l' or 'o':
        x += i
    if x == 'hello':
        print("YES")
        break;
    else:
        print("NO")