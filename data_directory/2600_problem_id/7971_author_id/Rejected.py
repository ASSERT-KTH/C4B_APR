n=int(input())
l = input()
l=[int(i) for i in l.split()]
l =sorted(l)
print(l[len(l//2)])