s = input()
S = s.split()
h1 = int(S[0])
h2 = int(S[1])
s = input()
S = s.split()
a = int(S[0])
b = int(S[1])
time = 14
if h1 + a*8 < h2 and a*12 <= b*12:
    print("-1")
elif h1 + a*8 >= h2:
    print("0")
else:
    h1 += a*8
    h1 -= b*12
    h1 += a*12
    if h1 >= h2:
        print("1")
    else:
        print(int((h2-h1)/(a*12 - b*12))+2)