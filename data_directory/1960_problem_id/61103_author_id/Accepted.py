for i in range(5):
    str = input().split()
    if '1' in str:
        print(abs(2-i)+abs(str.index('1')-2))