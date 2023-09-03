x = input()
x=int(x)
for i in[4,7,47,74,447,474,477,747,774]:
    if(x%i==0):
        print("YES")
        break
else:
    print("NO")