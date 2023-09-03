q,w=[int(x) for x in input().split()]
e=""
for i in range(q):
    if i<w:
        e += chr(ord('a')+i)
    else:
        e += 'a'
print(e)