n = int(input())
q = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
s = 1
d = 1
while n > 5*s:
    d+=1
    s = s *5
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