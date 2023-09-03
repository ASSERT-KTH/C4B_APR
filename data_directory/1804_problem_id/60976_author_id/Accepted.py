st = input()
a = set()
k = 0
for e in st:
    if not (e in a):
        k += 1
        a.add(e)
if k % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')