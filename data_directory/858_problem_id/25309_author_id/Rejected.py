n, p1, p2, p3 = (int(x) for x in input().split())
notebooks_needed = (4 - n % 4) % 4

price1 = p1 * notebooks_needed
price2 = p2 * (notebooks_needed // 2 + notebooks_needed % 2)
price3 = p2 * (notebooks_needed // 2) + p1
price4 = p3
best_price = min([price1, price2, price3, price4])

print(best_price)