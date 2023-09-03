x="ahhellllloou"
a=['h', 'e', 'l', 'l', 'o']
for i in x:
    if len(a)==0:
        break
    if i == a[0]:
        del a[0]
        
if len(a)==0:
    print("YES")
else:
    print("NO")