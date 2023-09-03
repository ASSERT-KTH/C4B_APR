def Digits(x):
    M = SumOfDigits(1)
    m = 1
    for i in range(2, x + 1):
        temp = SumOfDigits(i)
        if temp >= M and i > m:
            M = temp
            m = i
    return m
def SumOfDigits(n):
    return n % 10 + SumOfDigits(n//10) if n != 0 else 0    
print(Digits(int(input())))