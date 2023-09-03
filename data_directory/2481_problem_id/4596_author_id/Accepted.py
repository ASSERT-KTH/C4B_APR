n = int(input())
q = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
s = 5
d = 1
acc = 5
while n > acc:
    d = d * 2
    acc += (d *s) 
n -= (5 *(d-1))
if n <= d*1:
    print(q[0])
elif n <= d*2:
    print(q[1])
elif n <= d*3:
    print(q[2])
elif n <= d*4:
    print(q[3])
else:
    print(q[4])