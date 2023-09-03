n = input()
a = n.count("4") + n.count("7")
s = str(a)

for i in s:
    if  i != "4" and i != "7":
        print("NO")
        raise SystemExit
print("YES")