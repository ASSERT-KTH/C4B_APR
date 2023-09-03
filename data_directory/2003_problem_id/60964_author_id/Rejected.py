def main():
    n = int(input())
    for i in range(n + 1, 9000):
        numbers = set(str(i))
        if len(numbers) == 4:
            print(i)
            exit()


if __name__ == "__main__":
    main()