def get_ints(string):
    return list(map(int, string.split()))


def get_input():
    a = get_ints(input())
    return a


def sq_sum(sq):
    sq = list(sq)
    return sq[0].count('#') + sq[1].count('#')


def main():
    sq = []
    for _ in range(4):
        sq.append(input())

    for i in range(3):
        for j in range(3):
            new_sq = (sq[i][j:j+2], sq[i+1][j:j+2])
            if sq_sum(new_sq) in (1, 3):
                print('YES')
                return
    print('NO')

if __name__ == '__main__':
    main()