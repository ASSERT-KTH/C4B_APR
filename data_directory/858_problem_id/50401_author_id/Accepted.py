# cook your dish here
n, a, b, c = [int(n) for n in input().split()]
tempN = n
# If tempN is already a multiple of four
if tempN % 4 == 0:
    print(0)
    quit()
# otherwise, what would it take to make it a multiple of 4
k = 1
while True:
    tempN += 1
    if tempN % 4 == 0:
        break
    k += 1
# Sort out prices
prices = []
if k == 1:
    prices.append(a)
    prices.append(c + b)
    prices.append(3*c)
if k == 2:
    prices.append(b)
    prices.append(2*a)
    prices.append(2*c)
if k == 3:
    prices.append(c)
    prices.append(b + a)
    prices.append(3*a)

print(min(prices))