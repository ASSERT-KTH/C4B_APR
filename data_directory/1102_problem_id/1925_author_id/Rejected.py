cad = input().lower()
v = ['a', 'o', 'y', 'e', 't', 'i']
result = ""
for i in cad:
    if i in v:
        continue
    else:
        result = result + '.' + i
print(result)