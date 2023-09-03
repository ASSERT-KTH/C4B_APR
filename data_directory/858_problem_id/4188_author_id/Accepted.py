# print("Input n, a, b, and c")
n,a,b,c = [int(x) for x in input().split()]

if n%4 == 0:
    print(0)
elif n%4 == 3:  # Buy exactly one the only option.  NO!! Could be a two and a three!
    #  Or three tripletons!
    print(min(a, b + c, c*3))
elif n%4 == 2:  # Could buy two singletons or one doubleton OR TWO TRIPLETONS!
    print(min(a*2, b, c*2))
else:
    #  Same number of cases here I think...        
    print(min(a*3, b + a, c))