x, y = map(int, input().split())
while True:
    # Ciel prefers large coins.
    #print('available: %d * 10, %d * 1' % (x, y))
    a = min(2, x)
    x -= a
    b = min(22 - 10 * a, y)
    y -= b
    #print('Ciel takes %d * 10, %d * 1' % (a, b))
    if 10 * a + b < 22:
        print('Hanako')
        break

    # Hanako prefers small coins. 
    #print('available: %d * 10, %d * 1' % (x, y))
    # Start by maximizing the number of large coins.
    a = min(2, x)
    x -= a
    b = min(22 - 10 * a, y)
    y -= b
    if 10 * a + b < 22:
        print('Ciel')
        break
    # Exchange large coins for small.
    while a > 0 and y >= 10:
        a -= 1
        x += 1
        y -= 10
    #print('Hanako takes %d * 10, %d * 1' % (a, b))