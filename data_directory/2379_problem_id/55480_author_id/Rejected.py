a, b, c, d, e, f = map(int, input().split())
print('Ron' if a * e * c < f * d * b or (not c and d) or (not a and b and not d) else 'Hermione')