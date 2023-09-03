import math

n = int(input())
queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

c = 1
while 5 * c < n:
    n -= 5 * c
    c *= 2

print(queue[(n - 1) // c])