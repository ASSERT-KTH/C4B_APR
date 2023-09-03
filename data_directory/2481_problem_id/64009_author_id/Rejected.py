queue = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())

for _ in range(n):
    t = queue.pop(0)
    for _ in range(2):
        queue.append(t)

print(queue[-1])