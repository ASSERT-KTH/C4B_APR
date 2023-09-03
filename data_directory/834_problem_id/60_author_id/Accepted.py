import sys
input = sys.stdin.readline

players = int(input())
fib1 = 2
fib2 = 3

winner = 1

while True:
    cat = fib1
    fib1 = fib2
    fib2+=cat

    if fib1 > players:
        print(winner)
        break
    else:
        winner+=1