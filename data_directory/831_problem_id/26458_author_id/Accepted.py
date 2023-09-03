def isPrime(n):
    i = 2
    while i * i <= n:
        
        if n % i == 0:
            return False
        
        i += 1
    return True


def main():
    
    n = int(input())
    
    if isPrime(n) or n == 2:
        print(1)
    elif isPrime(n - 2) or n % 2 == 0 :
        print(2)
    else:
        print(3)
    
    
main()