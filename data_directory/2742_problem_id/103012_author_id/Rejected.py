def main():
    n = int(input())
    if n%2==0:
        print('1'*(n//2))
    else:
        n = n-3
        print('1'*(n//2), end="")
        print('7')


main()