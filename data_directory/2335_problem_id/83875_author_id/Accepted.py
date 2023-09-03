n = input()
string = "hello"
lt= []
m = 0
for i in n :
    if i == string[m]:
        m+=1
        if m == 5:
            print("YES")
            break
if m != 5:
    print("NO")