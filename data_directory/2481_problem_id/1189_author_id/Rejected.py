n = int(input())
names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

cnt = 1
while n > cnt * 5:
    n -= cnt * 5
    cnt += 1

print(names[(n - 1) // cnt])