l = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())
p = 0
sh = 0
w = 0
while True:
    w += 1
    p += 6
    if p>n:
        p -= 6
        print(l[((n-p-1)//w)%len(l)])
        break