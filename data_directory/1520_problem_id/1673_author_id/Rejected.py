n,a,b,c = list(map(int,input().split()))
D = [False]*(n+1)
D[0] = 0
for i in range(n+1):
    #yoftani D[i]
    javobho = []
    for x in {a, b, c}:
        try:
            if i >= x:
                javobho.append(D[i - x] + 1)
        except:
            pass
    if javobho:
        D[i] = max(javobho)
print(D[-1])