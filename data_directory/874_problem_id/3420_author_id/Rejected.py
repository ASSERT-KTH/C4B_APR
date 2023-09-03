n, k = map(int,input().split())
Size = 2**n
num = 1

i = 1
while i<=Size:
    for j in range(i,Size+1,i*2):
        if j ==k:
            print(num)
            exit()
    num+=1
    i=i*2