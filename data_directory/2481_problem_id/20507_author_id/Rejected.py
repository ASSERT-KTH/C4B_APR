n = int(input())
l = [0 , 1 , 2 , 3 , 4]
name = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
while n:
    n -=1
    p = l[0]
    l.append(p)
    l.append(p)
    l.pop(0)
print(name[p])