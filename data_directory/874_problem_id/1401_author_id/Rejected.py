n, k = map(int, input().split())

i = 2
while True:
    if k % i == (i // 2):
        print(i // 2)
        exit()
    i *= 2