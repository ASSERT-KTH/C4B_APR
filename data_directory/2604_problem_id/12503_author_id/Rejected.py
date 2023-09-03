n = int(input())
answer = n
if n >= 10:
    digits = []
    div = n
    while div != 0:
        div, mod = divmod(div, 10)
        digits.append(mod)
    sum1 = sum(digits)
    sum2 = digits[-1]-1+9*(len(digits)-1)
    if sum2 > sum1:
        variant1 = int(str(digits[-1]-1)+'9'*(len(digits)-1))
        variant2 = int(str(digits[-1])+'8'+'9'*(len(digits)-2))
        answer = variant1 if  variant2 > n else variant2
print(answer)