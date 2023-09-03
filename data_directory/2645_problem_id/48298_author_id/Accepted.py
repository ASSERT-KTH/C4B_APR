ls = [0, 1, 2]
n, x = int(input()), int(input())
for j in range(1, (n%6)+1):
    if j%2!=0:
        ls[0], ls[1] = ls[1], ls[0]
    else:
        ls[1], ls[2] = ls[2], ls[1]
print (ls[x])