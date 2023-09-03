simon, antisimon, celkom = map(int, input().split())
zobranych, vitaz = 0, True

while celkom > 0:
    if vitaz:
        hrac = simon
    else:
        hrac = antisimon

    for i in range(hrac):
        if hrac % (hrac - i) == 0 and celkom % (hrac - i) == 0:
            zobranych = hrac - i
            break

    celkom -= zobranych
    vitaz = not vitaz

if vitaz:
    print(1)
else:
    print(0)