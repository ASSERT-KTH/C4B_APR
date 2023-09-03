from fractions import Fraction
def Probability(ls):
    Y , W = ls
    num = 7 - max(Y,W)
    if num == 6:
        return '1/1'
    else:
        return str(Fraction(num, 6))
print(Probability(list(map(int, input().split()))))