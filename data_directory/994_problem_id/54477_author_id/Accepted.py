from math import ceil

def main():
    n, m, a = get_ints()
        
    result =ceil(n/a)*ceil(m/a)
    print (result)
    


def get_ints():
    return (int(x) for x in input().split(' '))


def get_ints_list():
    return list(int(x) for x in input().split(' '))


if __name__ == '__main__':
    main()