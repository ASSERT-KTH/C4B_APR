k = int(input())
months = sorted([int(x) for x in input().split(' ')])[::-1]
days = 0
while k > 0:
    k -= months[0]
    months = months[1:]
    days += 1

print(days)