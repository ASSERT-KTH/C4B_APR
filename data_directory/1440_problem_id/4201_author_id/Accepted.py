n = int(input())
result = n
while n != 1:
    a = 2
    while a * a <= n:
        if n % a == 0:
            break
        a += 1
    if a * a > n:
        n = 1
    else:
        n //= a
    result += n
print(result)