def main(n, m, a):
    width = n // a + (n % a > 0)
    length = m // a + (m % a > 0)
    return width * length

n, m, a = map(int, input().split(" "));
print(main(n, m, a));