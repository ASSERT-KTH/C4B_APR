a, b, c = map(int, input().split())
if c %2  != 0:
    p = 'L'
else:
    p = 'R'
nes = (c//(2*b))+1
if (c%(2*b) == 0):
    nes -=1
ost = b - (abs(c-2*nes*b)//2)
print(nes, ost, p)