from collections import deque


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

n = int(input())

queue = deque(names)

current = None

for drink in range(n):
    current = queue.popleft()
    queue.append(current)
    queue.append(current)

print(current)