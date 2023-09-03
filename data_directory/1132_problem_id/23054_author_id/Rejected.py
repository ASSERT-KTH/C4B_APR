x = input()
y=int(x)
if (all([x%i for i in[4,7,47,74,447,474,477,747,774]])):
    print("YES")
else:
    print("NO")