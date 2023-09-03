from collections import deque


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
# n_first_sheldon = [1, 6, 16, 36, 76, 156]
# space_between = [5, 10, 20, 40, 80, 160]
n_first_sheldon = []
space_between = []

x = -1
y = 1
z = 5
m = 0
while x < 10**9:
    n_first_sheldon.append(y)
    x = y
    z = 5*2**m
    space_between.append(z)
    y += z
    m += 1

n = int(input())

queue = deque(names)

current = None


def larger(n):
    for i in range(len(n_first_sheldon)):
        if n_first_sheldon[i] > n:
            return int(space_between[i-1]/5), n_first_sheldon[i-1], n_first_sheldon[i]

copies, start, nexter = larger(n)
# print(copies, start, nexter)

hue = n - start  # 3

magic = hue//copies
print(names[magic])


# for drink in range(n):
#     current = queue.popleft()
#     queue.append(current)
#     queue.append(current)
#     print(drink+1, "-", current)
#
# print(copies, start, nexter)