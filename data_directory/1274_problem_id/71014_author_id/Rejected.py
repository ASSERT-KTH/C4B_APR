def mod(dragon):
    for d in damage:
        if dragon % d == 0:
            return True

k, l, m, n, d = [int(x) for x in input().split()]
damage = [k, l, m, n]

dragons = list(range(1, d+1))
count_otpizzen = 0

for dragon in dragons:
    if mod(dragon):
        count_otpizzen += 1

print(count_otpizzen)