V = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'y', 'Y']

C = ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G',
     'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M',
     'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S',
     't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'z', 'Z']

s = [x for x in input() if x.isalpha()]

if s[-1] in V:   print('YES')
elif s[-1] in C: print('NO')