import os

LOCAL_PC = 'n1amr' in os.path.expanduser('~')


def process_file(in_name, out_name):
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            def read():
                return fin.readline().rstrip('\n')

            def write(*args, end='\n'):
                text = ' '.join(map(str, args)) + end
                fout.write(text)
                print(text, end='')

            t = int(fin.readline())
            for i in range(t):
                read()
                write('Case #{T}: \n'.format(T=i + 1), end='')
                solve(read, write)
                write()


def process_stdio():
    def read():
        return input()

    def write(*args, end='\n'):
        print(*args, end=end)

    solve(read, write)


def solve(input, print):
    a, b = map(int, input().split())
    diff = abs(a - b)
    if diff < 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    if LOCAL_PC:
        in_name = __file__[:-3] + '.in'
        out_name = __file__[:-3] + '.out'
        process_file(in_name, out_name)
    else:
        process_stdio()