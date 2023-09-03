num = int(input())

total = 2
if num == 0:
    print(0)
else:
    for i in range(num - 1):
        total = total * 2
    print(total)