chess = [input() for i in range(8)]
for c in chess:
    if 'WW' in c or 'BB' in c:
        print('NO')
        break
    else:
        continue
print('YES')