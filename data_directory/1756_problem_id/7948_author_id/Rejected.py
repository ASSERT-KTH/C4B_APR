shoes = [int(x) for x in input().split()]

count = 0

for shoe in shoes:
    if shoes.count(shoe) > 1:
        count += 1

print([0, count-1][count != 0])