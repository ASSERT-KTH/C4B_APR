string = input()
AEI = ('aeiouy')
BCD = ('bcdfghjklmnpqrstvwxz')
i = len(string) - 1
while (string[i] not in AEI) and (string[i] not in BCD):
    i -= 1
if string[i] in AEI:
    print('YES')
else:
    print('NO')