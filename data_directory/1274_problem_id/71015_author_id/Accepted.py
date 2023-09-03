k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

drag = list(range(1, d+1))

count = 0

for dr in drag:
    if dr % k == 0 or dr % l == 0 or dr % m == 0 or dr % n ==0:
        count += 1

print(count)