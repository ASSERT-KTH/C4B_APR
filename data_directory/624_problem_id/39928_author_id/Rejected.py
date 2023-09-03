start, increment, check = [int(x) for x in input().split(' ')]

f = (check - start) // increment - 1
l = (check - start) // increment + 1

out = []


for i in range(f, l):
    out.append(start + i * increment)

other = [x + 1 for x in out if x != start]

if check in out or check in other:
    print("YES")
else:
    print("NO")