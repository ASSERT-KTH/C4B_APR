x,y = [int(x) for x in input().split(" ")]
n = 0
while x <= y:
    n += 1
    x = x*3
    y = y*2
print(n)