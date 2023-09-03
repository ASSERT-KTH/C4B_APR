def main():
    n = int(input())
    for i in range(n, -1, -4):
        if not i % 7:
            print('4' * ((n - i) // 4) + '7' * (i // 7))
            return
    print(-1)


if __name__ == '__main__':
    main()