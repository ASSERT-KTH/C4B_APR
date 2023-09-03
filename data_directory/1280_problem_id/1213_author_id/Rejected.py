n = int(input())
A = input()
B = []
for i in A.split():
    B.append(int(i))
if n == 0:
    print(0)
else:
    B.sort(key=None, reverse=True)
    S = 0
    x = 0
    for j in B:
        S = S+j 
        x = x+1
        if S>=n:
            break
    print(x)