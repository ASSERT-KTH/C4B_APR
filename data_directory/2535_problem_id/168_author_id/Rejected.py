def convert_str_list_to_int(str_list):
    for i in range(len(str_list)):
        str_list[i] = int(str_list[i])
    return str_list


def main():
    input_str = input()
    inputs = convert_str_list_to_int(input_str.split(' '))
    n = inputs[0]
    m = inputs[1]

    walrus = 0
    sum = 0
    while True:
        if walrus > n:
            print('asdsdf')
            walrus = 0
            continue
        sum = sum + walrus
        walrus = walrus + 1

        m = m - walrus

        if m < 0:
            break
    print(m + n)


if __name__ == '__main__':
    main()