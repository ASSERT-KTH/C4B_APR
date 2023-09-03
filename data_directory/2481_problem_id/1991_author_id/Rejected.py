from collections import deque

n = int(input())
i = 1
link = deque()
link.append("Sheldon")
link.append("Leonard")
link.append("Penny")
link.append("Rajesh")
link.append("Howard")
while i < n:
    i = i + 1
    s = link.popleft()
    link.append(s)
    link.append(s)
print(link.popleft())