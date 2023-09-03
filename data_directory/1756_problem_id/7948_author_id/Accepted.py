shoes = [int(x) for x in input().split()]

distinct = []

count = 0

for shoe in shoes:
    if shoe in distinct:
        count += 1
    else:
        distinct.append(shoe)


print(count)