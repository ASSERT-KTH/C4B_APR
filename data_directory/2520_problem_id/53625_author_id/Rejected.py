from fractions import Fraction
def Probability(ls):
    Y , W = ls
    return str(Fraction(7 - max(Y,W), 6))
print(Probability(list(map(int, input().split()))))