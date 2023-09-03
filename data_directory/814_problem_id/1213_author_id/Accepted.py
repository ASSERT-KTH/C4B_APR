k,r = input().split()
k,r = int(k),int(r)
for i in range(1,1000):
    a = k*i%10
    if a == 0:
        print(i)
        break
    elif a == r:
        print(i)
        break