import sys
import math

def primes(number):
    size = number + 1
    lst = [True] * (number + 1)
    primeList = []
    for i in range(2, number):
        if lst[i] == False : continue 
        for j in range(i*2, size, i):
            if j < size and lst[j] == True and j % i == 0:
                lst[j] = False

    for i in range(size-1, 0, -1):
        if lst[i] == True :
            primeList.append(i)

    return primeList[:-1]
    

def solve(firstLine):
    n ,k  = firstLine[0], firstLine[1]
    primeList = primes(n)
    lst = [1] * (n + 1)

    for prime in primeList:
        lst[prime] += 1
        for i in range(prime * 2, n + 1 , prime):
            lst[i] = max([lst[i], lst[i-prime]]) + 1

    #print("test: ", lst)
    if lst[n] >= k:
        print("YES")
    else :
        print("NO")
        
    return

def main():
    firstLine = sys.stdin.readline().split()
    firstLine = list(map(int, firstLine))

    solve(firstLine)
    
if __name__ == "__main__":
    main()