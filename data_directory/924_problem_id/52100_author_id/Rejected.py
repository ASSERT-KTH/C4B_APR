a, b, c = map(int, input().split())
if c %2  != 0:
    p = 'L'
else:
    p = 'R'
nes = (c//(2*b))+1
if (c%(2*b) == 0):
    nes -=1
ost = round((c%(nes*b))/2)
if(ost == 0):
    ost = (c%(2*b*nes))//2
    if ost == 0:
        ost = b
print(nes, ost, p)