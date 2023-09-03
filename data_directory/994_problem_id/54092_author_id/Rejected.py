def main(n, m, a):
    width = n % a
    length = m % a
    return width * length

n, m, a = map(int, input().split(" "));
print(main(n, m, a));