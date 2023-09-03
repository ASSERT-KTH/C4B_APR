def mod(dragon):
    for d in damage:
        if dragon % d == 0:
            return True

damage = []
damage.append(int(input()))
damage.append(int(input()))
damage.append(int(input()))
damage.append(int(input()))
d = int(input())

dragons = list(range(1, d+1))
count_otpizzen = 0

for dragon in dragons:
    if mod(dragon):
        count_otpizzen += 1

print(count_otpizzen)