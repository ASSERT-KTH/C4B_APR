simon, antisimon, celkom = map(int, input().split())
zobranych, vitaz = 0, False

while celkom > 0:
    if vitaz: hrac = simon
    else: hrac = antisimon

    for i in range(hrac):
        if simon % (hrac - i) == 0 and celkom % (hrac - i) == 0:
            zobranych = hrac - i
            break

    celkom -= zobranych
    vitaz = not vitaz

if vitaz: print(0)
else: print(1)