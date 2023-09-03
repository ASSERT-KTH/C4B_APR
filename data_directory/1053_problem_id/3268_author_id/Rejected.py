def main():
    n = int(input())
    for i in range(n, -1, -7):
        if not i % 4:
            print('4' * (i // 4) + '7' * ((n - i) // 7))
            return
    print(-1)


if __name__ == '__main__':
    main()