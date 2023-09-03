k , r = [int(x) for x in input().split()]
number = 0
price = 0
shovel = 0

while shovel < k :
    shovel += 10

price = shovel -10

while True :
    if not (price + r) % k :
        price += r
        break
    elif price != 0 :
        if not price % k:
            break
    else :
        price += 10

print(int(price / k))