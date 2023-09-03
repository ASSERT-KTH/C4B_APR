inD = str(input()).split()
inD = [int(val) for val in inD]
k = inD[0]
a = inD[1]
b = inD[2]
N = 0
if (0 <= a <= b) or (a <= b <= 0):
    N = (b - a + 1)//k
if (a < 0) and (b > 0):
    N = -a//k + b//k + 1
print(N)