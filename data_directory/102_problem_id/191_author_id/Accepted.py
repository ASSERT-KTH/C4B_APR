a, b, c = map(int, input().split())
sum = []
sum.append(a+b+c)
sum.append(a*2 + b*2)
sum.append(a*2 + c*2)
sum.append(b*2 + c*2)
print(min(sum))