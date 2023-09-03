string = input()
AEI = ('aeiouy')
BCD = ('bcdfghjklmnpqrstvwxz')
i = len(string) - 1
while (string[i].lower() not in AEI) and (string[i].lower() not in BCD):
    i -= 1
if string[i].lower() in AEI:
    print('YES')
else:
    print('NO')