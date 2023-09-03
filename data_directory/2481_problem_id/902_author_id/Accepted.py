l = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())-1
p = 0
w = -1
while True:
    w += 1
    p += 5*(2**w)
    if p>n:
        p -= 5*(2**w)
        k = n-p
        print(l[k//(2**w)])
        break