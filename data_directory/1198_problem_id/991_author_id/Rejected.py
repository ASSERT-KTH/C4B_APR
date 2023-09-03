a=input()
b="HQ9+"
j=0
for i in a:
    if i in b:
        break
    j+=1
if len(a)==j:
    print("NO")
else:
    print("YES")