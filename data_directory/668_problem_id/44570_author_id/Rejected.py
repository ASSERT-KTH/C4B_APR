from sys import stdin

def main():
    uno = "I hate it"
    dos = "I love it"

    n = int(stdin.readline().strip())
    i = 1
    res = "I hate it"
    while i < n:
        if i%2 == 0:
            res = res +" that "+ uno
        else:
            res = res +" that "+ dos
        i += 1
    print(res)
    
main()