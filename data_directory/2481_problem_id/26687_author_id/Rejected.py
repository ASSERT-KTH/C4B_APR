a =int(input())
name=''
mas=[ "Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
for i in range(a):
    name = mas.pop(0)
    mas.append(name)
    mas.append(name)
print(name)