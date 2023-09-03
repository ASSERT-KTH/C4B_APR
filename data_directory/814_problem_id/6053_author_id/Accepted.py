k , r = [int(x) for x in input().split()]
number = 0
price = 0
shovel = 0

while shovel < k :
    shovel += 10

price = shovel -10
condition = True
while condition :
    if not (price + r) % k :
        price += r
        break
    else :
        price += 10
    if price != 0 :
        if not price % k:
            condition = False

print(int(price / k))