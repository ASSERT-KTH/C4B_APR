def main():
    n = int(input())
    i = n + 1
    while True:
        numbers = set(str(i))
        if len(numbers) == len(str(i)):
            print(i)
            exit()
        else:
            i += 1


if __name__ == "__main__":
    main()